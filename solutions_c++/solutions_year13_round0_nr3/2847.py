
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;
vector<int> precalculados;
int LIM = sqrt(1010);

int isCuad(int a){
    double b;
    b= sqrt(a);
    if(int(sqrt(a))-b == 0.0000000000000)
        return b;
    return 0;
}

bool isPal(int a){
    string tmp;
    while(a){
        tmp+= (a%10)+'0';
        a/=10;
    }
    for(int i=0,j=tmp.size()-1;i<(tmp.size())/2;i++,j--){
        if(tmp[i] != tmp[j])
            return false;
    }
    return true;
}

void preCalc(){
    int tmp=0;
    for(int i=1;i<1005;i++){
        if(isPal(i) and isCuad(i)){
            tmp = isCuad(i);
            if(isPal(tmp))
                precalculados.push_back(i);
        }
    }
}

int main(){
    preCalc();

    int T,ncas=0,l,r;
    vector<int>::iterator a,b;
    scanf("%d",&T);
    while(T--){
      int res=0;
      scanf("%d %d",&l,&r);
      /*a = lower_bound(precalculados.begin(),precalculados.end(),l);
      b = lower_bound(precalculados.begin(),precalculados.end(),r);
      */

      for(int i=0;i<precalculados.size();i++){
        if(precalculados[i]>=l and precalculados[i]<=r)
          res++;
      }


      printf("Case #%d: %d\n",++ncas,res);
    }

}
