#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

double cArr[100005];
double xArr[100005];

void genTable(double c,double f,double x,double cF){
    for(int i=0;i<100005;i++){
        cArr[i] = c/cF;
        xArr[i] = x/cF;
        cF += f;
    }
    
}
int main(){
    int n;
    double c,f,x;
    double result;
    double cF = 2;

    cin >> n;
    
    for(int i=1;i<=n;i++){
        memset(cArr,0,sizeof(c));
        memset(xArr,0,sizeof(x));
        cF = 2;
        result = 0;
        cin >> c >> f >> x;
        genTable(c,f,x,cF);
        
        //check
        //for(int i=0;i<12;i++){
        //    cout << i << ": " << cArr[i] << " " << xArr[i] << endl;
        //}
        
        
        int pt = 0;
        while(1){
            if((cArr[pt] + xArr[pt+1]) < xArr[pt])
                pt++;
            else
                break;
            
            //
            //cout << pt << endl;
            
        }
        for(int i=0;i<pt;i++){
            result += cArr[i];
        }
        result += xArr[pt];
        
        //cout << "CurrPt: " << pt << " ";
        printf("Case #%d: %.7f\n",i,result);
       // cout << "Case #" << i << ": " << result << endl;
    }
    
    
    
}