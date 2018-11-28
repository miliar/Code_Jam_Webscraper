#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>


using namespace std;

//#define DEBUG

#define LL long long
#define LD long double

bool check(long a, long b)
{
    return a > b;
}

struct node
{
  LL info;
  node * next;
};

int main()
{
#ifndef DEBUG
   freopen("A-small-attempt1(1).in","r",stdin);
 //  freopen("in.in","r",stdin);
   freopen("A3.out","w",stdout);
#endif
   int T,z;
   cin>>T;
   getchar();
   
   for(z =1; z<=T; z++)
   {
     string name;
     LL L;
     getline(cin,name,' ');
//     cout<<name.c_str()<<" "<<name.size()<<endl;
     
     cin>>L;
//     cout<<"L "<<L<<endl;
     getchar();


     LL i,j,k,cnt = 0;

     node * s = NULL, *p, *t;

     LL st = 0;
     for(i = 0; i< name.size();i++)
     {
//        cout<<"name "<<name[i]<<endl;
        if(name[i] == 'a' || name[i] == 'e' || name[i] == 'i' || name[i] == 'o' || name[i] == 'u')
        {
            st = 0;
            continue;
        }
        st++;
        if(st >= L)
        {
           p = (node*)malloc(sizeof(node));
           p->next = NULL;
           p->info = i-L+1;
#ifdef DEBUG
         cout<<"st "<<st<<" "<<p->info<<endl;
#endif
           if(s==NULL)
           {
              s = p;
           }
           else
              t->next = p;

           t = p;
          }
     }

     for(i =0; i<name.size(); i++)
     {
        for(j =i; j<name.size(); j++)      
        {
           node *p;
           for(p= s; p!=NULL; p=p->next)
           {
//               cout<<p->info<<endl;
               if(i<=p->info && j>=p->info+L-1)
               {  
//                  cout<<i<<" "<<j<<endl;
                  cnt++;
                  break;
               }
           }
        }
     }

       cout<<"Case #"<<z<<": "<<cnt<<endl;
   }

#ifdef DEBUG
  int xyz;
  cin>>xyz;
#endif

   return 0;
}

