#include <iostream>

using namespace std;

int main()
{
    int test,i,j,cnt;
    string s;
    //cout << "Hello world!" << endl;
    cin>>test;
    for(j=1;j<=test;j++){
        cin>>s;
        cnt=0;
        i=s.length()-1;
        while(s[i]=='+' && i>=0){
            i--;
        }
        if(i<0){
            cnt=0;
        }
        else{
            while(i>=0){
                while(i>0 && s[i]==s[i-1]){
                    i--;
                }
                cnt++;
                i--;
            }
        }
        cout<<"Case #"<<j<<": "<<cnt<<endl;
    }
    return 0;
}

