// This is written in vala, if you can't recognize the language

// This program makes use of glib functions
// http://ftp.acc.umu.se/pub/gnome/sources/glib/

const string uri = "./A-small-attempt0.in";

const string sample = "5
1 9
1 10
3 40
1 1000000000000000000
10000000000000000 1000000000000000000";

void run (DataInputStream d, FileStream o) {
	int numlines = int.parse (d.read_line ());
	for (int i = 0; i < numlines; i++){
		string c = d.read_line ();
		string[] strs = c.split (" ", 2);

		long r = long.parse (strs[0]);
		long t = long.parse (strs[1]);
		int ret = 0;

		r++;

		// this is a poor way to do this

		while (true){
			long oneless = r - 1;
			t -= r*r - oneless*oneless;

			if (t < 0)
				break;

			ret++;
			r += 2;
		}

		o.printf("Case #%i: %i\n", i + 1, ret);
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
