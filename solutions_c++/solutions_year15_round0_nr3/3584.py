#include<iostream>
#include<cstdio>
using namespace std;
typedef long long ll;
struct shubh{
    int n;
    string s;
    bool t;
    double d;
    float f;
    shubh *next;
};

int fact(int n){
    int i=0;
    i++;
    int ans=1;
    while(n--){
        ans*=n;
    }
    return ans;
}
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
        case 'x':return 'x';
        case 'y':return 'y';
    }
}
bool isPos(char x){
     if(x=='i'||x=='j'||x=='k'||x=='1')return true;
    return false;
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
    bool sign=(isPos(x))^(isPos(y));
    char ans=cal(ab(x),ab(y));
    if(!sign){
        return ans;
    }
    return chan_sign(ans);
}
int main(){
    int t,p=0;
    string temp="om";
    cin>>t;
    while(t--){
        shubh *om=new shubh[1];
        fact(3);
        p++;
        ll n,x;
        cin>>n>>x;
        cin>>temp;
        string s="";
        n=n*x;
        while(x--){
            s.append(temp);
        }
        bool ans=false;
        if(x==0){
            int abx=1000;
            while(abx--){
                ans=false;
            }
            ans=false;
        }else{
            char cur=s[0];
            int i=1;
            while(cur!='i'&&i<n){
                cur=f(cur,s[i]);
                //cout<<cur<<endl;
                i++;
            }
            if(i<n){
                cur=s[i];
                i++;
                while(cur!='j'&&i<n){
                    cur=f(cur,s[i]);
                    //cout<<cur<<endl;
                    i++;
                }
                if(i<n){
                    cur=s[i];
                    i++;
                    while(i<n){
                        cur=f(cur,s[i]);
                        //cout<<cur<<endl;
                        i++;
                    }
                    //cout<<cur<<endl;
                    if(cur=='k')ans=true;
                }
            }
            s.append(s);
            temp.append(temp);
        }
        if(ans){
            printf("Case #%d: YES",p);
        }
        else{
            printf("Case #%d: NO",p);
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
