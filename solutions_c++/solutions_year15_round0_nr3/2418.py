#include<iostream>
using namespace std;
typedef long long ll;
char chan_sign(char x){
    switch(x){
        case 'i':return 'a';
        case 'j':return 'b';
        case 'k':return 'c';
        case 'a':return 'i';
        case 'b':return 'j';
        case 'c':return 'k';
        case 'z':return '1';
        case '1':return 'z';
    }
}
bool isPos(char x){
    if(x=='a'||x=='b'||x=='c')return false;
    return true;
}
char neg(char x,char y){
    if(max(x,y)=='j')return 'k';
    if(min(x,y)=='i')return 'j';
    if(min(x,y)=='j')return 'i';
}
char cal(char x,char y){
    if(x==y)return 'z';
    char ans=neg(x,y);
    if(x=='i'&&y=='k')return chan_sign(ans);
    if(x=='j'&&y=='i')return chan_sign(ans);
    if(x=='k'&&y=='j')return chan_sign(ans);
    return ans;
}
char ab(char x){
    if(isPos(x))return x;
    return chan_sign(x);
}
char f(char x,char y){
    if(x=='1')return y;
    if(x=='z')return chan_sign(y);
    if(x==y)return 'z';
    if(y=='z')return chan_sign(x);
    bool sign=(isPos(x))^(isPos(y));
    char ans=cal(ab(x),ab(y));
    if(!sign){
        return ans;
    }
    return chan_sign(ans);
}
char power(char x,ll i){
    char ans='1';
    while(i--){
        ans=f(ans,x);
    }
    return ans;
}
int main(){
    int t,p=0;
    cin>>t;
    while(t--){
        p++;
        ll n,x;
        cin>>n>>x;
        ll len=n*x;
        string temp;
        cin>>temp;
        //x%=4;
        string s=temp;
        char l='1';
        for(int i=0;i<n;i++){
            l=f(l,s[i]);
        }
        ll pow=x%4;
        bool ans=false;
        s="";
        ll four=4;
        int count=min(four,x);
        n*=count;
        while(count--){
            s.append(temp);
        }
        //cout<<s;
        //cout<<power(l,pow)<<endl;
        if(power(l,pow)=='z'){
            //cout<<"-1 found"<<endl;
            ll cnti=0,cntj=0;
            char cur=s[0];
            cnti++;
            int i=1;
            while(i<n&&cur!='i'){
                cur=f(cur,s[i]);
                cnti++;
                i++;
            }
            //cout<<cur;
            if(cur=='i'){
                //cout<<"i found"<<endl;
                cur=s[n-1];
                cntj++;
                //cout<<s[n-1];
                ll j=n-2;
                while(j>0&&cur!='k'){
                   // cout<<cur;
                    cur=f(s[j],cur);
                    cntj++;
                    j--;
                }
            }
            //cout<<cur;
            if(cur=='k')ans=true;
            if(cnti+cntj>=len)ans=false;
        }
        if(ans)cout<<"Case #"<<p<<": YES";
        else{
            cout<<"Case #"<<p<<": NO";
        }
        cout<<endl;
    }

   /* char cur='1';
    while(1){
        char temp;
        cin>>temp;
        cur=f(cur,temp);
        cout<<cur<<endl;
    }*/

}
