#include <bits/stdc++.h>
using namespace std;

#define FOR(p,star,end) for(int p = star ; p<end ; p++)
#define FORR(p,star,end) for(int p = star ; p>=end ; p--)
#define INF 1000000000
#define MOD 1000000007
#define MAX 1002

#define pii pair<int ,int >
#define vi vector<int>
#define vii vector< pair<int ,int> >
#define pb push_back
#define mp make_pair
#define ll long long
char mat1[300][300];
int mat2[300][300];
string str;
int dp[10010][3];
bool post[10010];
bool prefix[10010];

char ANS [3]= {'i','j','k'};
vi A;

int Can(int loc, int phase )
{

    if(phase == 2)
        return (int)(post[loc]);

    if(dp[loc][phase]!=-1)
        return dp[loc][phase];

    char cur = str[loc];
    int sign=0;

    if(cur == ANS[phase])
        if(Can((int)loc+1,(int)phase+1))
            return dp[loc][phase]=1;

    FOR(i,loc+1,str.size())
    {

        sign^=mat2[cur-'0'][str[i]-'0'];
        cur= mat1[cur-'0'][str[i]-'0'];

        if(cur == ANS[phase] && sign==0 )
            if(Can(i+1,phase+1))
                return dp[loc][phase]=1;

    }

    return dp[loc][phase]=0;
}
int main()
{


  freopen("C-small-attempt9.in","r",stdin);
   freopen("out.txt","w",stdout);


    mat1['1'-'0']['1'-'0']='1';
    mat2['1'-'0']['1'-'0']=0;

    mat1['1'-'0']['i'-'0']='i';
    mat2['1'-'0']['i'-'0']=0;


    mat1['1'-'0']['j'-'0']='j';
    mat2['1'-'0']['j'-'0']=0;

    mat1['1'-'0']['k'-'0']='k';
    mat2['1'-'0']['k'-'0']=0;


    mat1['i'-'0']['1'-'0']='i';
    mat2['i'-'0']['1'-'0']=0;

    mat1['i'-'0']['i'-'0']='-1';
    mat2['i'-'0']['i'-'0']=1;

    mat1['i'-'0']['j'-'0']='k';
    mat2['i'-'0']['j'-'0']=0;

    mat1['i'-'0']['k'-'0']='-j';
    mat2['i'-'0']['k'-'0']=1;


    mat1['j'-'0']['1'-'0']='j';
    mat2['j'-'0']['1'-'0']=0;

    mat1['j'-'0']['i'-'0']='-k';
    mat2['j'-'0']['i'-'0']=1;

    mat1['j'-'0']['j'-'0']='-1';
    mat2['j'-'0']['j'-'0']=1;

    mat1['j'-'0']['k'-'0']='i';
    mat2['j'-'0']['k'-'0']=0;


    mat1['k'-'0']['1'-'0']='k';
    mat2['k'-'0']['1'-'0']=0;

    mat1['k'-'0']['i'-'0']='j';
    mat2['k'-'0']['i'-'0']=0;

    mat1['k'-'0']['j'-'0']='-i';
    mat2['k'-'0']['j'-'0']=1;

    mat1['k'-'0']['k'-'0']='-1';
    mat2['k'-'0']['k'-'0']=1;


    int t;
    cin >> t;
    FOR(tc,1,t+1)
    {
        int l,x;
        cin >> l >> x ;
        cin >> str;
        string temp = str;

        FOR(i,0,x-1)
            str+=temp;

        fill(&post[0],&post[str.size()+ 10],false);
        fill(&prefix[0],&prefix[str.size() + 10],false);

        int N = str.size()-1;
        post[N]= (bool)(str[N]=='k');
        char lastRes = str[N],cur;
        int sign =0;
        FORR(i,N-1,0)
        {
            cur = str[i];
            sign^=mat2[cur-'0'][lastRes-'0'];
            lastRes= mat1[cur-'0'][lastRes-'0'];


            post[i] = (bool)( (lastRes =='k') && (!sign) ) ;
        }

        prefix[0]=(bool)(str[0]=='i');
        cur = str[0];
        sign =0;
        FOR(i,1,str.size())
        {

            sign^=mat2[cur-'0'][str[i]-'0'];
            cur= mat1[cur-'0'][str[i]-'0'];

            prefix[i] = (bool)( (cur =='i') && (!sign) )  ;
        }


        FOR(i,0,str.size())
        if(prefix[i])
            A.pb(i);


        int res=0;
        fill(&dp[0][0],&dp[str.size() + 10][0],-1);
        FOR(i,0,A.size())
        {

            res|=Can(A[i]+1,1);
            if(res)
                break;
        }


        printf("Case #%d: ",tc);
        if(res==0)
            printf("NO\n");
        else
            printf("YES\n");


        A.clear();
    }


    return 0;


}





