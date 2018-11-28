#include<iostream>
#include<cstdio>
#include<stdlib.h>

using namespace std;

#define iFor(i,n) for(int i=0;i<=n;i++)
#define iFor2(i,n,m) for(int i=n;i<=m;i++)
#define iForDesc(i,n) for(int i=n;i>=0;i--)

string ijk[8][4] = {"1","i","j","k",
                    "i","-1","k","-j",
                    "j","-k","-1","i",
                    "k","j","-i","-1",
                    "-1","-i","-j","-k",
                    "-i","1","-k","j",
                    "-j","k","1","-i",
                    "-k","-j","i","1",
                    };

int GetRowCol(string test){
   if(test.compare("1")==0){
       return 0;
   }else if(test.compare("i")==0){
       return 1;
   }else if(test.compare("j")==0){
       return 2;
   }else if(test.compare("k")==0){
       return 3;
   }else if(test.compare("-1")==0){
       return 4;
   }else if(test.compare("-i")==0){
       return 5;
   }else if(test.compare("-j")==0){
       return 6;
   }else if(test.compare("-k")==0){
       return 7;
   }
}

int N;
#define SMALL
//#define LARGE

int main(){
   freopen("a.txt","rt",stdin);
   #ifdef SMALL
        freopen("C-small-attempt2.in","rt",stdin);
        freopen("C-small.out","wt",stdout);
   #endif
   #ifdef LARGE
	    freopen("B-large-practice.in","rt",stdin);
	    freopen("B-large.out","wt",stdout);
   #endif

   cin>>N;
   int L=0,X=0;
   string s,wrep;
   iFor2(i,1,N){
       printf("Case #%d: ",i);
       L=0,X=0;
       cin>>L>>X;
       getline(cin,s);
       s="";
       wrep = "";
       getline(cin,s);
       iFor2(j,1,X){
           wrep = wrep + s;
       }
       int round= 0;
       string check = "i";
       string ch="",ch2="";
           int counter=0;
       int row=0,col=0;
       ch=wrep.at(counter);
       while(true){
            if(counter==(L*X-1)){
                  break;
            }
            if(ch.compare(check)==0){
                round++;
                ch = wrep.at(++counter);
                if(round==1)
                    check="j";
                else if(round==2)
                    check = "k";
                else
                    check = "d";
            }else{
                ch2 = wrep.at(++counter);
                row = GetRowCol(ch);
                col = GetRowCol(ch2);
                ch = ijk[row][col];

            }

       }
       if(round==2 && ch.compare(check)==0){
            cout<<"YES\n";
       }else if(round==3 &&  GetRowCol(ch)==0){
           cout<<"YES\n";
       }else{
           cout<<"NO\n";
       }

   }

}
