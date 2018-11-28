#include <iostream>
#include <string>
using namespace std;
int main() {
    int MAX_L=11;
    int T;
    int L;
    char s[MAX_L];
    char h[1];
    char x;
    int time;
    cin>>T;
    cin.getline(h,1);
    int Thold=T;
    while(T>0){
        cin.getline(s,11);
        L=(int)strlen(s);
        x=s[0];
        time=0;
        for(int i=0;i<L;i++){
            if(x==s[i])
                continue;
            else{
                time++;
                x=s[i];
            }
        }
        if(x=='-')
            time++;
        cout<<"Case #"<<Thold-T+1<<": "<<time<<endl;
        T--;
    }
    return 0;
}
