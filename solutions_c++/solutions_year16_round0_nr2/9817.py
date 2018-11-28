#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main() {
  int T;
  cin >> T;
  int i = 1;
  while ( i <= T) {
    int res = 0;
    string s;
    cin >> s;
    int len = s.length();
    int startpos = 0;
    int endpos = len - 1;
    if (startpos == endpos) {
        s[startpos]=='-' ?  res = 1 : res = 0;
    }
    else {

        while(startpos < endpos){
                //cout<<startpos<<":"<<endpos<<endl;
                if (s[startpos] != s[startpos+1]) {
                    reverse(s.begin(), s.begin() + startpos+1);
                    //cout<<"reversed:"<<s<<endl;
                    replace(s.begin(), s.begin() + startpos+1, '-','*');
                    replace(s.begin(), s.begin() + startpos+1, '+','-');
                    replace(s.begin(), s.begin() + startpos+1, '*','+');

                    res++;
                    //cout<<s<<endl;
                }

                startpos++;

        }
        if(s[endpos] == '-') {
            reverse(s.begin(), s.begin() + startpos+1);
                    //cout<<"reversed:"<<s<<endl;
            replace(s.begin(), s.begin() + startpos+1, '-','*');
            replace(s.begin(), s.begin() + startpos+1, '+','-');
            replace(s.begin(), s.begin() + startpos+1, '*','+');

            res++;
            //cout<<s<<endl;
        }


    }

    cout <<"Case #"<<i<<": "<<res<<endl;
    i++;
  }
}
