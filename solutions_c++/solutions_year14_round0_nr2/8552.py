#include<iostream>
#include<cstdio>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<algorithm>
#include<cmath>
#include<string>
#include<bitset>
#include<memory.h>
#include<cassert>
#include<ctime>


class string_operations
{
      private :
              long long Ppower[16000];
               long long length;
               std::vector <long long> power,hash;
               std::vector<std::vector<char> > bor;
               long long HashConst,AlphabetSize;
      public:
             std::string CurrentString;
             inline void Assign(std::string s)
             {
                  CurrentString = s,HashConst = 29LL,AlphabetSize=30;
                  length =  s.size();
                  power.resize(length+1),hash.resize(length+1);
                  power.clear(),hash.clear();
             }
             void BuildHash()
             { 
                  power[0] = 1;
                  for(int i = 0 ; i < length; i ++ )
                   hash[i+1] = (hash[i] + (long long)(CurrentString[i]-'a'+1)*power[i]),
                   power[i+1]=power[i]*HashConst;
             }
             inline long long get(int l,int r)
             {
                        return ((long long)(hash[r]-hash[l-1])*power[length-r]);
             }
             inline bool EqualSubstring(int l1,int r1,int l2,int r2)
             {
                  if (l1>l2) std::swap(l1,l2),std::swap(r1,r2);
                  if (r2-l2!=r1-l1) return 0;
                  return (get(l1,r1)==get(l2,r2));
             }
             int InString(int len , long long Right, long long H)
             {
                 int ans = 0;
                 long long Q = std::max(Right , length);
                 for (int i = 1 ; i <= length - len + 1; i ++ )
                  if (H*Ppower[Q-Right] == get(i,i+len-1)*Ppower[Q-length]) ans++;
                 return ans;
             }
};

class Cartesian_Tree
{
      private:
              int size ,root ,MAXSIZE;
              struct Cartesian
              {
                     int random_priority,
                         left_son,right_son,
                         size;
                     long long Value,Sum,Min,Max;
                     Cartesian(){};
                     Cartesian(long long _Value):random_priority(rand()%50000000),left_son(0),right_son(0),size(1),
                                        Value(_Value),Sum(_Value),Min(_Value),Max(_Value){};
              };
              std::vector<Cartesian> D;
              int AddInTree(int root , long long x)
              {
                   D[++size] = Cartesian(x);
                   return Merge(root , size);
                   //root = Merge(root , size);
              }
              int Update_Values(int vertex)
              {
                  if (vertex == 0) return 0;
                  D[vertex].size = D[D[vertex].left_son].size + 1 + D[D[vertex].right_son].size;
                  D[vertex].Sum = D[D[vertex].left_son].Sum + D[D[vertex].right_son].Sum + D[vertex].Value;
                  D[vertex].Min = std::min(std::min(D[D[vertex].left_son].Min,D[D[vertex].right_son].Min),D[vertex].Value);
                  D[vertex].Max = std::max(std::max(D[D[vertex].left_son].Max,D[D[vertex].right_son].Max),D[vertex].Value);
                  return vertex;
              }
              int Merge(int left,int right)
              {
                  if (left == 0 || right == 0)
                   return left + right;
                  int Result;
                  if (D[left].random_priority > D[right].random_priority)
                       D[left].right_son = Merge(D[left].right_son, right),
                       Result = left;
                  else
                       D[right].left_son = Merge(left , D[right].left_son),
                       Result = right;
                  return Update_Values(Result);
              }
              void Split(int Vertex,int Value,int &Left,int &Right)
              {
                   if (Vertex == 0)
                    return void(Left = Right = 0);
                   if (D[D[Vertex].left_son].size + 1 <= Value) 
                    Split(D[Vertex].right_son,Value-D[D[Vertex].left_son].size-1,D[Vertex].right_son,Right) , Left = Vertex;
                   else
                    Split(D[Vertex].left_son,Value,Left,D[Vertex].left_son) , Right = Vertex;
                   Update_Values(Vertex);
              }
      public:
             void Build(int SIZE,std::vector<long long> &a)
             {
                  MAXSIZE = SIZE , root = size = 0;
                  D.assign(MAXSIZE+5 , 0);
                  D[0].size = 0;
                  srand(31415);
                  for (int i = 1 ; i < a.size() ; i ++ )
                   root = AddInTree(root , a[i]);
             }
             /*void Print()
             {
                  cout<<"zero"<<D[0].size<<endl;
                  cout<<"root: "<<root  << endl;
                  For(i,1,size)
                   cout << i << " " << D[i].left_son << " " << D[i].right_son <<" " << D[i].Sum <<" " << D[i].size <<endl;
             }*/
             Cartesian Get(int left_board,int right_board)
             {
                       int C1=0,C2=0,C3=0;
                       Split(root,right_board,C2,C3);
                       Split(C2,left_board-1,C1,C2);
                       Cartesian Ans = D[C2];
                       C2 = Merge(C1,C2);
                       root = Merge(C2,C3);
                       return Ans;
             }
             void Update(int number, int New_Value)
             {
                  int C1,C2,C3;
                  Split(root,number,C2,C3);
                  Split(C2,number-1,C1,C2);
                  C1 = AddInTree(C1 , New_Value);
                  root = Merge(C1,C3);
             }
};     
class Fenwick_tree
{
      private:
              std::vector<long long> t;
              int size;
              long long get0(int l)
              {
                   long long res = 0;
                   for (; l>0 ;l = (l&(l+1)) - 1)
                       res += t[l];
                   return res;
              }
      public:
             void Assign(int n)
             {
                  size = n;
                  t.assign(size + 1 , 0);
             }
             void Clear()
             {
                  for (int i = 1; i <= size; i ++ )
                   t[i] = 0;
             }
             void Erase()
             {
                  int size = 0;
                  t.clear();
                  t.resize(0);
             }
             void Build(std::vector<long long> &a)
             {
                  for (int i = 1 ;i <= size ;i ++ ) 
                      update(i,a[i]);
             }
             long long get(int l,int r)
             {
                  return get0(r) - get0(l-1);
             }
             void update(int r,long long x)
             {
                  for ( ; r <= size; r |=(r+1))
                      t[r]+=x;
             }
};
class Interval_tree
{
      private:
              int size; 
              struct record
              {
                     int l,r;
                     long long minimal_value,maximal_value,dest , add , Equal;
                     bool isEqualed;
                     record(){};
                     record(int _l,int _r,long long _minimal_value,long long _maximal_value,long long _dest,long long _add,long long _Equal,bool _isEqualed):
                                l(_l),r(_r),minimal_value(_minimal_value),maximal_value(_maximal_value),dest(_dest),add(_add),Equal(_Equal),isEqualed(_isEqualed){};                                
              };
              std::vector<record> tree; 
              record CriticalF ;
              void InBuild(std::vector<long long> &a,int v ,int l,int r)
              {
                   tree[v] = record(l,r,(long long)2e18,(long long)-2e18,0,0,0,0);
                   if (l == r) tree[v].dest = tree[v].minimal_value = tree[v].maximal_value = a[l];
                   else
                   {
                       int m = (l + r)/2;
                       InBuild(a,v+v,l,m);
                       InBuild(a,v+v+1,m+1,r);
                       tree[v] = Combine(tree[v+v],  tree[v+v+1]);
                   }
              }
              void push(int v)
              {
                   if (tree[v].l == tree[v].r) return;
                   if (tree[v].isEqualed){
                       tree[v].isEqualed = 0;
                       tree[v+v].isEqualed = tree[v+v+1].isEqualed = 1;
                       tree[v+v].Equal = tree[v+v+1].Equal = tree[v].Equal;
                       tree[v].dest=(tree[v].r-tree[v].l+1)*tree[v].Equal;
                       tree[v].minimal_value = tree[v].maximal_value = tree[v].Equal;
                   }
                   if (tree[v].add){
                       tree[v].minimal_value += tree[v].add;
                       tree[v].maximal_value += tree[v].add;
                       tree[v].dest += (tree[v].r-tree[v].l+1)*tree[v].add;
                       tree[v+v].add += tree[v].add;
                       tree[v+v+1].add += tree[v].add;
                       tree[v].add = 0;
                   }
              }
              record Combine(record first, record second)
              {
                     //if (first.isEqualed || first.add) push(first);
                     //if (second.isEqualed || second.add) push(second);
                     if (first.isEqualed) first.minimal_value = first.maximal_value = first.Equal,first.dest = (first.r-first.l+1)*first.Equal;
                     if (first.add) first.minimal_value+=first.add, first.maximal_value+=first.add, first.dest += (first.r-first.l+1)*first.add;
                     if (second.isEqualed) second.minimal_value = second.maximal_value = second.Equal,second.dest = (second.r-second.l+1)*second.Equal;
                     if (second.add) second.minimal_value+=second.add, second.maximal_value+=second.add, second.add += (second.r-second.l+1)*second.add;
                     return record(first.l,second.r,std::min(first.minimal_value,second.minimal_value),std::max(first.maximal_value,second.maximal_value),
                     first.dest+second.dest,0,0,0);
              }
      public:
             void Build(std::vector<long long> &a,int n)
             {
                  size = n;
                  CriticalF = record(1,size,(long long)2e18,(long long)-2e18,0,0,0,0);
                  tree.resize(4*size + 1 );
                  InBuild(a,1,1,n);
             }
             record get(int v, int l, int r)
             {
                  if (l>r) return CriticalF;
                  if (tree[v].add || tree[v].isEqualed) push(v);
                  if (tree[v].l == l && tree[v].r == r)
                      return record(l,r,tree[v].minimal_value,tree[v].maximal_value,tree[v].dest,tree[v].add,tree[v].Equal,tree[v].isEqualed);
                  int m = (tree[v].l + tree[v].r)>>1;
                  return Combine( get(v+v,l,std::min(r,m)) , get(v+v+1,std::max(m+1,l),r) );     
             }
             void update_sum(int v,int l,int r,long long Value)
             {
                  if (tree[v].add || tree[v].isEqualed) push(v);
                  if (tree[v].l == l && tree[v].r == r)
                   return(void( tree[v].add+=Value ));
                  int m = (tree[v].l + tree[v].r)>>1;
                  if (l <= m) update_sum(v+v,l,std::min(r,m),Value);
                  if (r > m) update_sum(v+v+1,std::max(m+1,l),r,Value);
                  if (tree[v+v].add || tree[v+v].isEqualed) push(v+v);
                  if (tree[v+v+1].add || tree[v+v+1].isEqualed) push(v+v+1);
                  tree[v] = Combine(tree[v+v], tree[v+v+1]);
             }
             void update_equal(int v,int l,int r,long long Value)
             {
                  if (tree[v].add || tree[v].isEqualed) push(v);
                  if (tree[v].l == l && tree[v].r == r)
                  {
                     tree[v].isEqualed = 1 , tree[v].Equal = Value;
                     return ;
                  }
                  int m = (tree[v].l + tree[v].r)>>1;
                  if (l <= m) update_equal(v+v,l,std::min(r,m),Value);
                  if (r > m) update_equal(v+v+1,std::max(m+1,l),r,Value);
                  if (tree[v+v].add || tree[v+v].isEqualed) push(v+v);
                  if (tree[v+v+1].add || tree[v+v+1].isEqualed) push(v+v+1);
                  tree[v] = Combine( tree[v+v] , tree[v+v+1] );
             }
};
class MathAlgo
{
     private:
     
     public:
            long long gcd(long long a,long long b)
            {
                 a = abs(a) , b = abs(b);
                 while (a > 0 && b > 0)
                  if (a > b) a %= b;
                  else
                   b %= a;
                  return a + b;
            }
            long long lcm(long long a,long long b)
            {
                 long long d = gcd(a,b);
                 return (a / d) * b;
            }
            int gcd(int a,int b)
            {
                a = abs(a) , b = abs(b);
                while (a > 0 && b > 0)
                 if (a > b) a %= b;
                 else
                  b %= a;
                return a + b;
            }
            long long lcm(int a,int b)
            {
                 int d = gcd(a , b);
                 return (a / d) * b;
            }
            bool isPrime(int x)
            {
                 for (int i = 2; i * i <= x ; i ++ )
                     if (x%i == 0)
                      return 0;
                 return (x>1);
            }
            long long BinPower(long long basic,long long degree)
            {
                 long long answer = 1;
                 for (;degree;degree>>=1)
                 {
                     if (degree&1) answer *= basic;
                     basic*=basic;
                 }
                 return answer;
            }
            long long BinPowerMod(long long basic,long long degree,int Mod = 1000000007)
            {
                 //const int Mod = 1000000007;
                 long long answer = 1;
                 basic%=Mod;
                 for (;degree;degree>>=1)
                 {
                     if (degree&1) answer = (answer * basic)%Mod;
                     basic = (basic * basic)%Mod;
                 }
                 return answer;
            }
            std::vector<long long> getPrimeList(int MaxNumber)
            {
                        std::vector<long long> Prime,Lp(MaxNumber+1,0);
                        for (int i = 2 ;i <= MaxNumber ; i ++ )
                        {
                            if (Lp[i] == 0) Prime.push_back(i) , Lp[i] = i;
                            for (int j = 0 ; j < Prime.size() && Prime[j] <= Lp[i] && Prime[j]*i <= MaxNumber; j ++ )
                                Lp[Prime[j]*i] = Prime[j];
                        }
                        return Prime;
            }
            std::vector<long long> getLeastDividersList(int MaxNumber)
            {
                        std::vector<long long> Prime(MaxNumber+1,0),Lp(MaxNumber+1,0);
                        int PrimeCount = 0;
                        for (int i = 2 ;i <= MaxNumber ; i ++ )
                        {
                            if (Lp[i] == 0) Prime[PrimeCount++] = i , Lp[i] = i;
                            for (int j = 0 ; j < PrimeCount && Prime[j] <= Lp[i] && Prime[j]*i <= MaxNumber; j ++ )
                                Lp[Prime[j]*i] = Prime[j];
                        }
                        return Lp;
            }
            void getSqueezeCoords(long long a[],int l,int r)
            {
                 std::vector<std::pair<long long,long long> > b(r-l+1);
                 for (int i = l; i <= r ; i ++ )
                  b[i-l] = std::make_pair(a[i],i-l);
                 sort(b.begin(), b.end());
                 int FillcharIter = 1;
                 for (int i = 0 ;i <= r-l;)
                 {
                     int j = i, startVal = b[i].first;
                     while (j <= r-l && b[j].first == startVal)
                           b[j++].first = FillcharIter;
                     FillcharIter++;
                     i = j;
                 }
                 for (int i = 0 ; i <= r-l; i ++ )
                  std::swap(b[i].first,b[i].second);
                 sort(b.begin(),b.end());
                 for (int i = 0 ; i <= r-l ; i ++ )
                  a[i+l] = b[i].second;
            }
            long long EulerFunction(long long n)
            {
                long long res = n;
                for (long long i  = 2 ; i * (long long) i <= n ; i ++)
                {
                    if (n%i == 0)
                    {
                            res = (res / i) * (i-1);
                            while (n%i == 0) n/=i; 
                    }
                }
                if (n > 1) res = (res / n)*(n-1);
                return res;
            }
};
//================================================================== */
#include<iostream>
#include<cstdio>
#include<stack>
#include<queue>
#include<set>
#include<iomanip>
#include<complex>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>
#include<string>
#include<bitset>
#include<memory.h>
#include<cassert>
#include<ctime>
 
 
#pragma comment(linker, "/stack:30000000")
 
using namespace std;
 
#define For(i,l,r) for (int i = l ;i < (int)(r + 1) ; ++ i )
#define ForI(it , s , T) for (T :: iterator it = s.begin(); it != s.end() ; ++ it )
#define LL long long
#define iinf 2000000000
#define linf 2000000000000000000LL
#define MOD  1000000007
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)
#define pb(x) push_back(x)
#define mk(x,y) make_pair(x,y)
#define sqr(x) ((x)*(x))
#define pause cin.get();cin.get();
#define fin freopen("input.txt","r",stdin)
#define fout freopen("output.txt","w",stdout)
#define fir first
#define sec second
#define ln(x) log(x)
 
const int Direct[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
const int Nmax = 200000;

const double eps =1e-8;
double Solve()
{
       double C,dF,X;
       cin >> C >> dF >> X;
       double Counts = 0 , F = 2;
       double MinTime = X / F;
       double UsedTime = 0;
       for (int Houses = 1 ; abs(F - X) > eps; Houses ++)
       {
           double RangeTime = (C - Counts) / F;
           if (RangeTime < -eps) RangeTime = 0;
           UsedTime += RangeTime;
           if (Counts + eps < C) Counts = C;
           Counts -= C;
           F += dF;
           double RemainingTime = (X - Counts) / F;
           if (RemainingTime < -eps) RemainingTime = 0;
           MinTime = min(MinTime , UsedTime + RemainingTime);
           if (UsedTime > MinTime + eps) break;
       }
       return MinTime;
}
string getNumber(int x)
{
       string res ="";
       while (x > 0)
       {
             res += (char)(x%10 + 48);
             x/=10;
       }
       reverse(res.begin(),res.end());
       return res;
}
int main()
{ 
   ios_base::sync_with_stdio(0);
   //freopen("B-large.in","r",stdin);
   //freopen("B-large.out","w",stdout);
   int T;
   cin >> T;
   cout.precision(8);
   for (int it = 1 ;it <= T ; it ++)
   {
       string sample = "Case #" + getNumber(it) + ": ";
       cout << sample << fixed << Solve() << endl;
   }
   return 0;
} 
