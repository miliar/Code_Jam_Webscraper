#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<math.h>
#include<stdint.h>
//#include<Insst.h>
using namespace std;
//typedef Insst LL;

int value(char c)
{
    int x = c;
    return x-64;
}

main() {

	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	string s, ss;

	for(int t = 1; t <= T; t++){

            cin >> s;
            	cout << "Case #" << t << ": ";
            ss = s[0];
            int pointer = value(s[0]);
          //  cout<<"\n"<<s.length();
            for(int j=1; j<s.length();j++)
            {
                if(pointer>value(s[j]))
                {
                    ss += s[j];
                }
                else{

                    ss = s[j] + ss;
                    pointer = value(s[j]);
                }
            }
 		cout << ss << endl;

		}
//		cout << "Case #" << t << ": ";
//		cout << add << endl;


}
