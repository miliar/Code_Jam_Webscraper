#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

bool isPalindromes(int a){
    stringstream ss;
    string stra;
    ss << a;
    ss >> stra;
    int i =0 , j = stra.length()-1;
    while( i <= j){
        if(stra[i]!=stra[j]) break;
        i++;j--;
    }
    if(i<=j) return false;
    else return true;
}

bool isSquare(int a){
    int b = sqrt(a);
    if(abs(a-b*b) < 1e-8) return true;
    else return false;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("3333ans.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int iCase = 1; iCase <= T; iCase ++ ){
        int A,B;
        scanf("%d %d",&A,&B);
        int cnt = 0;
        for(int i = A; i<=B; i ++){
            if(isSquare(i)&& isPalindromes(i) && isPalindromes(int(sqrt(i)))) cnt++;

        }
        printf("Case #%d: ",iCase);
        printf("%d\n",cnt);
    }
    return 0;
}
