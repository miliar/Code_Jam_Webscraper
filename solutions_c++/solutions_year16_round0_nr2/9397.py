#include<bits/stdc++.h>
using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
string s;
int siz;
void removePlus(){
    reverse(s.begin(),s.end());
    for(int i=0;i<s.size();i++){
        if(s[i]=='+'){
            s.erase(s.begin());
            i--;
        }
        else
            break;
        if(s.size()==0)
            break;
    }
    reverse(s.begin(),s.end());
}
void rev(int x){
    for(int i=0;i<=x;i++){
        s[i]= (s[i]=='-'?'+':'-');
    }
    reverse(s.begin(), s.end()-(siz-(x+1)));
}
void flip(){
    for(int i=0;i<siz;i++){
        s[i]= (s[i]=='-'?'+':'-');
    }
    reverse(s.begin(),s.end());
}
int main()
{
    //READ("B-large.in");
    //WRITE("B-large.out");
    int i,t,n=0;
    bool check=false;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>s;
        n=0;
        while(1){
            removePlus();
            siz=s.size();
            if(siz==0)
                break;
            check = false;
                if(s[0]=='-')
                    check=true;
            if(check == true){
                flip();
                //cout<<s<<" - \n";
            }
            else{
                for(int j=siz-1;j>=0;j--){
                    if(s[j]=='+'){
                        rev(j);
                        //cout<<s<<" +\n";
                        break;
                    }
                }
            }
            n++;
        }

        cout<<"Case #"<<i<<": "<<n<<"\n";
    }

}
