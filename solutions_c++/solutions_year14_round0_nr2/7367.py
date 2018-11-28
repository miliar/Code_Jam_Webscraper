#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int t = 0;t<n;t++){
        double c, f, x;
        cin>>c>>f>>x;
        double curr = 2;
        double next = curr+f;
        double res = 0;
        //Magic
        while((x-c)/curr>x/next){
            res += c/curr;
            curr = next;
            next = curr+f;
        }
        res += x/curr;
        printf("Case #%d: %.7f\n",t+1, res);
    }
}
