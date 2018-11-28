#include<cstdio>
#include<iostream>
#include<cstring>
#include<ctime>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<cmath>
#include<algorithm>
#include<map>
#define lowbit(x) (x)&(-x)
#define maxn 1000010
#define ls (o)<<1
#define rs ((o)<<1)|1
#define mod 142857
typedef long long ll;
using namespace std;
#define N 40000
struct node{
    int s,e;
    node(int ss,int ee):s(ss),e(ee){}
};
map<string,string>mp;
void init()
{
    mp["ii"]="-1";mp["ij"]="k";mp["ik"]="-j";
    mp["ji"]="-k";mp["jj"]="-1";mp["jk"]="i";
    mp["ki"]="j";mp["kj"]="-i";mp["kk"]="-1";
    mp["-ii"]="1";mp["-ij"]="-k";mp["-ik"]="j";
    mp["-ji"]="k";mp["-jj"]="1";mp["-jk"]="-i";
    mp["-ki"]="-j";mp["-kj"]="i";mp["-kk"]="1";
}
string func(string a,char b)
{
    string res="";
    if(a[0]=='1')return res+b;
    if(a[0]=='-'&&a[1]=='1')return res+'-'+b;
    a+=b;
    return mp[a];
}
bool ok(string s1,string s2)
{
    if(s1[0]=='i'&&s2[0]=='k')return true;
    if(s1[0]=='1'&&s2[0]=='-'&&s2[1]=='j')return true;
    if(s1[0]=='-'&&s1[1]=='1'&&s2[0]=='j')return true;
    if(s1[0]=='j'&&s2[0]=='-'&&s2[1]=='1')return true;
    if(s1[0]=='-'&&s1[1]=='j'&&s2[0]=='1')return true;
    if(s1[0]=='k'&&s2[0]=='-'&&s2[1]=='i')return true;
    if(s1[0]=='-'&&s1[1]=='k'&&s2[0]=='i')return true;
    if(s1[0]=='-'&&s2[0]=='-'&&s1[0]=='i'&&s2[0]=='k')return true;
    return false;
}
string s,rr[10005],fr[10005],str;
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output_C.txt","w",stdout);
    init();
    int t,x,l,p=0;
    scanf("%d",&t);
    while(p++<t){
        str="";
        vector<int>ei,sk;
        scanf("%d%d",&x,&l);
        cin>>s;
        for(int i=0;i<l;i++)str+=s;
        int len = str.length();
        rr[len]="1";
        string tt="";
        for(int i=len-1;i>=0;i--){
            tt="";
            if(rr[i+1][0]=='1'||rr[i+1][1]=='1')rr[i]=func(rr[i+1],str[i]);
            else if(rr[i+1][0]=='-'){
                tt+='-';tt+=str[i];
                rr[i]=func(tt,rr[i+1][1]);
            }
            else{
                tt+=str[i];
                rr[i]=func(tt,rr[i+1][0]);
            }
            if(rr[i][0]=='k')sk.push_back(i);
            //cout<<rr[i]<<endl;
        }
        fr[0]="";fr[0]+=str[0];if(str[0]=='i')ei.push_back(0);
        //cout<<fr[0]<<endl;
        for(int i=1;i<len;i++){
            fr[i]=func(fr[i-1],str[i]);
            if(fr[i][0]=='i')ei.push_back(i);
            //cout<<fr[i]<<endl;
        }
        //cout<<str<<endl;
        int flag=0,l1=ei.size(),l2=sk.size();
        if(l1==0||l2==0){
            printf("Case #%d: NO\n",p);
            continue;
        }
        //cout<<l1<<" "<<l2<<endl;
        for(int i=0;i<l1;i++){
            for(int j=0;j<l2;j++){
                //cout<<ei[i]<<" "<<sk[j]<<endl;
                if(ei[i]>=sk[j])continue;
                //cout<<fr[ei[i]]<<" "<<fr[sk[j]-1]<<endl;
                if(ok(fr[ei[i]],fr[sk[j]-1])){
                    flag=1;
                    break;
                }
            }
            if(flag)break;
        }
        if(flag)printf("Case #%d: YES\n",p);
        else printf("Case #%d: NO\n",p);
        //for(int i=0;i<ei.size();i++)printf("%d ",ei[i]);printf("\n");

    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
