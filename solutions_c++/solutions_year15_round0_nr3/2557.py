#include<bits/stdc++.h>

#define FOR(i,a,b) for(auto i=a; i!=b+1-2*(a>b); i+=1-2*(a>b))
#define REP(i,a,b) for(auto i=a-(a>b); i!=b-(a>b); i+=1-2*(a>b))
#define ALL(v) v.begin(),v.end()
#define what_is(x) cout<<#x<<" is "<<x<<endl;
#define min3(a,b,c) min(min(a,b),c)
#define max3(a,b,c) max(max(a,b),c)
#define SIZE 10000
#define MAXN 1000000007
#define PI 3.141592653589793
#define open_read1 freopen("C:\\Users\\Hepic\\Desktop\\a.txt","r",stdin)
#define open_write1 freopen("C:\\Users\\Hepic\\Desktop\\b.txt","w",stdout)
#define open_read freopen("ariprog.in","r",stdin)
#define open_write freopen("ariprog.out","w",stdout)

using namespace std;


typedef long long LL;
typedef pair<int,int> PII;


int T,L,X;
int pos1,pos2,pos3;
bool found;
char letr1,letr2,letr3;
int sign1,sign2,sign3;
string inp,word;



char counts(char lt1, int &sign, char lt2)
{
    if(lt1=='1')
        return lt2;


    else if(lt1=='i')
    {
        if(lt2=='1')
            return 'i';

        else if(lt2=='i')
        {
            sign*=-1;
            return '1';
        }

        else if(lt2=='j')
            return 'k';

        else if(lt2=='k')
        {
            sign*=-1;
            return 'j';
        }
    }


    else if(lt1=='j')
    {
        if(lt2=='1')
            return 'j';

        else if(lt2=='i')
        {
            sign*=-1;
            return 'k';
        }

        else if(lt2=='j')
        {
            sign*=-1;
            return '1';
        }

        else if(lt2=='k')
            return 'i';
    }


    else if(lt1=='k')
    {
        if(lt2=='1')
            return 'k';

        else if(lt2=='i')
            return 'j';

        else if(lt2=='j')
        {
            sign*=-1;
            return 'i';
        }

        else if(lt2=='k')
        {
            sign*=-1;
            return '1';
        }
    }
}



int main()
{
    open_read1;
    open_write1;


    scanf("%d",&T);


    FOR(t,1,T)
    {
        scanf("%d%d",&L,&X);
        cin>>inp;


        found=false;
        word="";
        FOR(i,1,X)
            word += inp;



        if(word.size()<3)
        {
            printf("Case #%d: NO\n",t);
            continue;
        }


        pos1=0;
        letr1=word[pos1];
        sign1=1;
        while((letr1!='i' || sign1!=1) && pos1+1<word.size())
            letr1 = counts(letr1, sign1, word[++pos1]);

        if(pos1>=word.size())
        {
            printf("Case #%d: NO\n",t);
            continue;
        }


        pos2=pos1+1;
        letr2=word[pos2];
        sign2=1;
        while((letr2!='j' || sign2!=1)  && pos2+1<word.size())
            letr2 = counts(letr2, sign2, word[++pos2]);

        if(pos2>=word.size())
        {
            printf("Case #%d: NO\n",t);
            continue;
        }



        pos3=pos2+1;
        letr3=word[pos3];
        sign3=1;
        while(pos3+1<word.size())
            letr3 = counts(letr3, sign3, word[++pos3]);


        if(letr3=='k' && sign3==1)
             printf("Case #%d: YES\n",t);
        else
            printf("Case #%d: NO\n",t);
    }



    return 0;
}
