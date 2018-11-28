#include <iostream>
#include <string>

using namespace std;

class Frag {
public:
	string s;
	long long l;
	long long x;
	long long sloc;
	long long xcount;
	Frag(long long Ell, long long Ecks, string Ess): l(Ell), x(Ecks), s(Ess) {
		sloc=0;
		xcount=1;
	};
	char Next() {
		if (sloc==l) {
			xcount++;
			if (xcount>x) return '0';
			sloc=0;
		}
		sloc++;
		return s[sloc-1];
	};
	void Skip() {
		if (x-xcount > 4)
			x=xcount + ((x-xcount) % 4);
	};
};

char Calc(char x, char y) {
	// i j k a b c - 1
	switch(x) {
		case 'i':
			switch(y) {
				case 'i':
					return '-';
					break;
				case 'j':
					return 'k';
					break;
				case 'k':
					return 'b';
					break;
				case 'a':
					return '1';
					break;
				case 'b':
					return 'c';
					break;
				case 'c':
					return 'j';
					break;
				case '1':
					return 'i';
					break;
				case '-':
					return 'a';
					break;
				default:
					cout << "BAD DATA!";
			}
			break;
		case 'j':
			switch(y) {
				case 'i':
					return 'c';
					break;
				case 'j':
					return '-';
					break;
				case 'k':
					return 'i';
					break;
				case 'a':
					return 'k';
					break;
				case 'b':
					return '1';
					break;
				case 'c':
					return 'a';
					break;
				case '1':
					return 'j';
					break;
				case '-':
					return 'b';
					break;
				default:
					cout << "BAD DATA!";
			}
			break;
		case 'k':
			switch(y) {
				case 'i':
					return 'j';
					break;
				case 'j':
					return 'a';
					break;
				case 'k':
					return '-';
					break;
				case 'a':
					return 'b';
					break;
				case 'b':
					return 'i';
					break;
				case 'c':
					return '1';
					break;
				case '1':
					return 'k';
					break;
				case '-':
					return 'c';
					break;
				default:
					cout << "BAD DATA!";
			}
			break;
		case 'a':
			switch(y) {
				case 'i':
					return '1';
					break;
				case 'j':
					return 'c';
					break;
				case 'k':
					return 'j';
					break;
				case 'a':
					return '-';
					break;
				case 'b':
					return 'k';
					break;
				case 'c':
					return 'b';
					break;
				case '1':
					return 'a';
					break;
				case '-':
					return 'i';
					break;
				default:
					cout << "BAD DATA!";
			}
			break;
		case 'b':
			switch(y) {
				case 'i':
					return 'k';
					break;
				case 'j':
					return '1';
					break;
				case 'k':
					return 'a';
					break;
				case 'a':
					return 'c';
					break;
				case 'b':
					return '-';
					break;
				case 'c':
					return 'i';
					break;
				case '1':
					return 'b';
					break;
				case '-':
					return 'j';
					break;
				default:
					cout << "BAD DATA!";
			}
			break;
		case 'c':
			switch(y) {
				case 'i':
					return 'b';
					break;
				case 'j':
					return 'i';
					break;
				case 'k':
					return '1';
					break;
				case 'a':
					return 'j';
					break;
				case 'b':
					return 'a';
					break;
				case 'c':
					return '-';
					break;
				case '1':
					return 'c';
					break;
				case '-':
					return 'k';
					break;
				default:
					cout << "BAD DATA!";
			}
			break;
		case '-':
			switch(y) {
				case 'i':
					return 'a';
					break;
				case 'j':
					return 'b';
					break;
				case 'k':
					return 'c';
					break;
				case 'a':
					return 'i';
					break;
				case 'b':
					return 'j';
					break;
				case 'c':
					return 'k';
					break;
				case '1':
					return '-';
					break;
				case '-':
					return '1';
					break;
				default:
					cout << "BAD DATA!" << endl;
			}
			break;
		case '1':
			return y;
			break;
		default:
			cout << "BAD DATA 2! " << x << " " << y <<endl;
	}
}

int main() {
	//cout<< Calc('1','i') << endl;
	//cout << Calc('i','1') << endl;
	//return(0);
  int cases=0;
  cin >> cases;
  int caseNum=0;
  while (caseNum < cases) {
    caseNum++;
    int L=0;
    cin >> L;
    long long X=0;
    cin >> X;
    string text;
    cin >> text;
    Frag frag(L,X,text);
    char cur='1';
    char next='1';
    while (cur!='0' && cur!='i') {
	    next=frag.Next();
	    if (next=='0') 
		    cur='0';
	    else
		    cur=Calc(cur,next);
    }
    if (cur!='0') cur='1';
    while (cur!='0' && cur!='j') {
	    next=frag.Next();
	    if (next=='0')
		    cur='0';
	    else
		    cur=Calc(cur,next);
    }
    if (cur!='0') cur='1';
    frag.Skip();
    if (cur!='0') {
	    while (next!='0') {
		    next=frag.Next();
		    if (next=='0') {
			    if (cur!='k') cur='0';
		    } else
			    cur=Calc(cur,next);
	    }
    }
    if (cur=='k')
      cout << "Case #" << caseNum << ": YES" << endl;
    else
      cout << "Case #" << caseNum << ": NO" << endl;
  }
  return 0;
}

