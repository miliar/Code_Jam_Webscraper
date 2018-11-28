// This is written in vala, if you can't recognize the language

// This program makes use of glib functions
// http://ftp.acc.umu.se/pub/gnome/sources/glib/

const string uri = "C-small-attempt0.in";

const string sample = "3
1 4
10 120
100 1000";

class decary{
	// Little endian base ten numbers
	protected char[] d;

	public decary (){
		d = new char[1];
		d[0] = 1;
	}

	public decary.from_string (string s){
		int len = s.length;
		d = new char[len];
		for (int i = len - 1; i >= 0; i--){
			d[len - 1 - i] = s[i] - '0';
		}
	}

	public void set_as_square (decary a){
		d.resize (a.d.length * 2 + 1);
		for (int i = 0; i < d.length; i++)
			d[i] = 0;

		int len = a.d.length;
		for(int i = 0; i < len; i++){
			for(int j = 0; j < len; j++){
				d[i+j] += a.d[i] * a.d[j];
			}
		}

		int len2 = d.length;
		int regroup = 0;
		for (int i = 0; i < len2; i++){
			regroup += d[i];
			d[i] = (char)(regroup % 10);
			regroup /= 10;
		}

		int lastzero;
		for (lastzero = len2; (d[lastzero-1] == 0 && lastzero >= 1); lastzero--);
		d.resize (lastzero);
	}

	public string to_string (){
		char[] c = new char[d.length + 1];
		int len = d.length;
		for (int i = len - 1; i >= 0; i--){
			c[i] = '0' + d[len - 1 - i];
		}
		c[d.length] = 0;
		return (string) c;
	}

	public void inc(){
		int len = d.length;
		bool remainder = true;
		for (int i = 0; remainder; i++){
			if (len <= i)
				d.resize (++len);
			d[i] += 1;
			if (d[i] < 10)
				remainder = false;
			else
				d[i] -= 10;
		}
	}

	public bool is_palindrome(){
		int lst = d.length - 1;
		for(int i = d.length / 2; i >= 0; i--){
			if (d[lst - i] != d[i])
				return false;
		}
		return true;
	}

	public bool is_greater(decary a){
		if (this.d.length > a.d.length)
			return true;
		if (this.d.length < a.d.length)
			return false;
		for (int i = this.d.length - 1; i >= 0; i--){
			if (this.d[i] > a.d[i])
				return true;
			if (this.d[i] < a.d[i])
				return false;
		}
		return false;
	}

	public bool is_lesser(decary a){
		if (this.d.length > a.d.length)
			return false;
		if (this.d.length < a.d.length)
			return true;
		for (int i = this.d.length - 1; i >= 0; i--){
			if (this.d[i] > a.d[i])
				return false;
			if (this.d[i] < a.d[i])
				return true;
		}
		return false;
	}
}

int fairsquares (decary start, decary end){
	int ret = 0;

	bool notthereyet = true;
	decary s = new decary ();
	decary sq = new decary ();
	for (; !sq.is_greater (end); s.inc()){
		if (!s.is_palindrome())
			continue;
		sq.set_as_square (s);
		//stdout.printf ("%s\n", sq.to_string ());
		if (!sq.is_palindrome())
			continue;
		if (notthereyet && sq.is_lesser (start))
			continue;
		notthereyet = false;
		//stdout.printf ("%s\n", sq.to_string ());
		if (!sq.is_greater (end))
			ret++;
	}

	return ret;
}

void run (DataInputStream d, FileStream o) {
	int numlines = int.parse (d.read_line ());
	for (int i = 0; i < numlines; i++){
		string c = d.read_line ();
		string[] strs = c.split (" ", 2);

		int val = fairsquares (new decary.from_string (strs[0]), new decary.from_string (strs[1]));

		o.printf("Case #%i: %i\n", i + 1, val);
	}
}

int main () {
	if (uri == ""){
		// testing
		var input = new MemoryInputStream.from_data (sample.data, null);
		var d = new DataInputStream (input);
		run (d, stdout);
	} else {
		// run
		var o = FileStream.open ("./" + Log.FILE + ".res", "w");
		var input = File.new_for_path (uri);
		var d = new DataInputStream (input.read ());
		run (d, o);
	}
	return 0;
}
