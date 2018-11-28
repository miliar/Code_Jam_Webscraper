//just header ....
using namespace std;
#include<bits/stdc++.h>


///=========================================FOR TAKING INPUT OF ANY TYPE , till 4 parameter====================================================

///inline void make(string &a) { string s ; if(scanf("%s",s)); a = s; }
inline void make(int &a)
{
    if(scanf("%d", &a));
}
inline void make(float &a)
{
    if(scanf("%f", &a));
}
inline void make(double &a)
{
    if(scanf("%lf", &a));
}
inline void make(char *a)
{
    if(scanf("%s", a));
}
inline void make(char &a)
{
    if(scanf(" %c", &a));
}
inline void makec(char &a)
{
    if(scanf("%c", &a));
}

template<typename A, typename B> inline void make(pair<A, B> & p)
{
    make(p.first);
    make(p.second);
}
template<typename A>
inline void maketab(A *tab, int size)
{
    for(int i = 0; i < size; i++) make(tab[i]);
}
template<typename A>
inline void maketab(vector<A> &v, int size)
{
    typedef typename vector<A>::iterator iter;
    v.resize(size);
    for(iter i = v.begin(); i != v.end(); i++) make(*i);
}

template<typename A, typename B>
inline void make(A &a, B &b)
{
    make(a);
    make(b);
}
template<typename A, typename B, typename C>
inline void make(A &a, B &b, C &c)
{
    make(a);
    make(b);
    make(c);
}
template<typename A, typename B, typename C, typename D>
inline void make(A &a, B &b, C &c, D &d)
{
    make(a);
    make(b);
    make(c);
    make(d);
}
template<typename A, typename B, typename C, typename D, typename E>
inline void make(A &a, B &b, C &c, D &d, E &e)
{
    make(a);
    make(b);
    make(c);
    make(d);
    make(e);
}





/// ==========================================================  FOR LESS WRITING OF ll, vector,pair, map , push,size,traverse objects===================
typedef long long       ll;
typedef vector<int>     vi;
typedef vector<vi>      vvi;
typedef pair<int, int>  ii;
typedef vector<ii>      vii;
typedef vector<vii>     vvii; //think about 2D matrix of pair
typedef set<int>        si;
typedef map<string,int> msi;
typedef unsigned long long llu;


///size, push
#define sz(a) int((a).size())
#define pb push_back




///traverse all container
#define all(c) c.begin(),c.end()



///attention .... it is not ............standard ....so it will not work...try to omit this.....
///loop through all container
#define tr(c,it)\
            for(typeof(c.begin()) it=(c).begin();it!=(c).end();it++)

///=============================================================== FOR USING FOR LOOP, (FORALL,FOR) ============================================
#define FORALL(i,a,b) for(int i=(a);i<=(b);++i)
#define FOR(i,n) for(int i=0;i<(n);++i)
#define FORB(i,a,b) for(int i=(a);i>=(b);--i)


//abs of any numbers
#define abs(x) (((x) < 0) ? - (x) : (x))
#define sq(x) x*x
//value of pi
#define PI 2*acos (0.0)
//}
//typedef long long ll;

#define mem(a,v) memset(a,v,sizeof(a)) //need to see in the internet

#define OC printf("Case %d:",i)


int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0 (1).in","r",stdin);
    //freopen("out.txt","w",stdout);
    /*
    int a;
    make(a);
    //getchar();
    FORALL(i,1,a)
    {
        int input;
        string str;
        make(input);
        getchar();
        getline(cin,str);
        int sum = 0;
        FORALL(j,0,input-1)
        {
            //if(str[j]=='0')sum++;
        }
        printf("Case #%d: %d\n",i,sum);



    }
    */

    int T;
    make(T);
    FORALL(t,1,T)
    {
        int n;string person;
        make(n);
        getchar();
        getline(cin,person);
        int stand = 0;
        int require = 0;
        int sum = 0;
        int level[n+2];
        FOR(i,n+1){
            level[i] = i;
        }

        FOR(i,n+1){
        //cout << "tesst" << level[i] << " ";
        }
        stand = person[0] - '0';
        //cout << endl;
        FORALL(i,1,n)
        {
            //cout << "i " <<i << endl;
            if(person[i] - '0' == 0)continue;
            //else if( 7)cout << "not working" << endl;

            else if(level[i] > stand ){
                require+=level[i] -stand;
                stand+=require + person[i] - '0';
                //cout << require << endl;
            }
            else if(level[i] <= stand)
            {
                stand+=person[i] - '0';
            }
            //cout << " "<<require << " " << i << " stand " << stand <<endl;
        }
        printf("Case #%d: %d\n",t,require);


    }

    return 0;
}



















