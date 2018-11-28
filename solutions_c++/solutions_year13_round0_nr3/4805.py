#include<iostream>                 //------------------------------------------------------------//
#include<stdio.h>                  //  ___  ___ _____ ______                                     //
#include<algorithm>                //  |  \/  |/  ___|| ___ \     This C++ Template Belongs to   //
#include<math.h>                   //  | .  . |\ `--. | |_/ /        Manish Singh Bisht          //
#include<vector>                   //  | |\/| | `--. \| ___ \                                    //
#include<set>                    //  | |  | |/\__/ /| |_/ /    Email: manish05@facebook.com    //
#include<map>                    //  \_|  |_/\____/ \____/                                     //
#include<string>                 //------------------------------------------------------------//

using namespace std;

#define gc getchar_unlocked
#define MEM(a,b) memset(a,(b),sizeof(a))
#define FOR(i,n) for(int i=(0);i<(n);i++)
#define CLEAR(a) memset((a),0,sizeof(a))
#define S(n) scanf("%d", &n)
#define P(k) printf("%d\n", k)
#define fastS(n) scanint(&n)
#define pb push_back
#define mp make_pair
#define ll long long
#define VI vector<int>
#define PII pair<int, int>
#define ft first
#define sd second
#define inf (1<<30)
#define PNL printf("\n")
#define SP system("pause")
#define md 1000000007
#define PII pair<int, int>
#define mxx 1000000000
#define swap(a,b) {*b = (*a + *b) - (*a = *b);}
#define fout cout
#define fin cin

int ispalin(long long n)
{
    long long temp,p,sum=0;
    p=n;
    while(temp=p%10)
    {
        p/=10;
        sum=sum*10+temp;        
    }
   if(n==sum)
   return 1;
   else
   return 0;
    
}

std::vector<long long> FS;

int tell_index(long long x,int l)
{
 int last=FS.size()-1;
 int first=0;
 int mid;

 while(first<=last)
 {
  mid=(first+last)/2;

  if(FS[mid]==x)
  return mid+l;
  else if(x>FS[mid])
  first=mid+1;
  else
  last=mid-1;
 }

 return mid;
}

int main()
{

//ifstream fin;fin.open("data.in",ios::in);
//ofstream fout;fout.open("data.out",ios::out);

   int t=0;
   fin>>t;


   for(long long i=0;i<10000000;i++)
   {
   long long pp=i*i;
    if(ispalin((ll)i) && ispalin(pp))
    {
    FS.pb(pp);
    //fout<<pp<<"\t";
    }

   }



   for(int i=0;i<t;i++)
   {

   long long a,b;
   fin>>a>>b;
   
   long long ans= tell_index(b,1)-tell_index(a,0);
       fout<<"Case #"<<i<<": "<<ans<<endl;
   }


 //  fin.close();
 //  fout.close();
    return 0;
}
