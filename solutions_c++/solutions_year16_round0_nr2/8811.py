//Coder: Karthikeyan Arulmozhivarman

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <stdio.h>
#include <conio.h>


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

char pile[102];

void flip( int head, int next)
{
     if(pile[head] == '-') {
        pile[head] = '+';              
     }   else {
        pile[head] = '-';
     }    
     fr(i,next+1) {
        pile[i] = pile[head];       
     }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large-out.txt", "w", stdout);
    int T,t;
    int c;

    unsigned int N, M, count = 1,i;
    scanf("%d", &T);
    c = getchar();
    for(t = 1; t <= T; t++) {
      i = 0;
      c = 'a';
      count = 0;
          
      while(c!='\n') {
         c = getchar();
         pile[i] = c;
         i++;          
         //printf("c=%c\n",c);  
      }    
      
      pile[i-1] = 'E';
      pile[i] = '\0';
      int head = 0, next = 0,pivot=1;
      //printf("init  %s.\n",pile);    
    
      while(count<=100){
         if(pile[pivot] == 'E') {
            if(pile[head] == '-') {
               flip(head, next);
               count++;           
            }             
            //printf("pivot hit E\n");
            break;
         } else if ( pile[next] == pile[pivot]) {
            next++; pivot++;   
            //printf("pivot same\n");
         } else if (pile[next] != pile[pivot]) {
            flip(head, next);
            count++;    
            //printf("pivot different\n");
         }
         //printf("changes, %s.\n",pile);        
      }
     printf("Case #%d%: %d\n",t,count); 
    }
    
    getch();
	return 0;
}
