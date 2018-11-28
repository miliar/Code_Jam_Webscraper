#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cTime>
#include <string.h>

using namespace std;
#define MAX 1005

float K[MAX],N[MAX];
float sortedK[MAX],sortedN[MAX];
int n;
bool Nb[MAX],Kb[MAX];

bool isBig(float val){
    for(int i=0 ; i<n ; i++){
        if(!Kb[i] && sortedK[i]>val){
            Kb[i]=true;
            return true;
        }
    }
    for(int i=0 ; i<n ; i++)
        if(!Kb[i]){
            Kb[i]=true;
            return false;
        }
    return false;
}
int minPosition;
float getMin(){
    for(int i=0 ; i<n ; i++){
            if(!Kb[i]){
                minPosition=i;
                return sortedK[i];
            }
    }
}
bool isPossible(float minK){
    for(int i=0 ; i<n ; i++){
        if(!Nb[i] && sortedN[i]>minK){
            Nb[i]=true;
            return true;
        }
    }
    return false;
}
bool isDBig(int pos,float val){
    float minK=getMin();
    if(isPossible(minK)){
        Kb[minPosition]=true;
        return true;
    }else {
        for(int i=n-1 ; i>=0 ; i++){
            if(!Kb[i]){
                Kb[i]=true;
                Nb[pos]=true;
                return false;
            }
        }
    }
    return false;
}
int playDWar(){
    memset(Nb,false,sizeof(Nb));
    memset(Kb,false,sizeof(Kb));
    int count=0;
    for(int i=0 ;  i<n ; i++){
       if(isDBig(i,sortedN[i]))
            count++;
    }

    return count;
}

int playWar(){
    memset(Nb,false,sizeof(Nb));
    memset(Kb,false,sizeof(Kb));
    int count=0;
    for(int i=0 ; i<n ; i++){
        if(!isBig(sortedN[i])){
            count++;
            //cout<<sortedN[i]<<endl;
        }
    }
    return count;
}
void print(){

    for(int i=0 ; i<n ; i++)
        cout<<sortedN[i]<<" ";
    cout<<endl;
    for(int i=0 ; i<n ; i++)
        cout<<sortedK[i]<<" ";
    cout<<endl;
}
int main()
{
	int testCases;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	//freopen("D-small-attempt1.in","r",stdin);
	//freopen("D-small-attempt1.out","w",stdout);
	cin>>testCases;
	for(int k=1 ; k<=testCases ; k++){
       cin>>n;
       for(int i=0 ; i<n ; i++){
            cin>>sortedN[i];
            N[i]=sortedN[i];
       }
       sort(sortedN,sortedN+n);
       for(int i=0 ; i<n ; i++){
           cin>>sortedK[i];
            K[i]=sortedK[i];
       }
       sort(sortedK,sortedK+n);
        //print();
        cout<<"Case #"<<k<<":"<<" "<<playDWar()<<" "<<playWar()<<endl;
	}
	return 0;
}


