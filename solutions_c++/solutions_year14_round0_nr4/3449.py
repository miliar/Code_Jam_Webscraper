#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
double num[1005],num2[1005];
int main (){
    int T,N;
    int a1,a2;
    scanf("%d",&T);
    for(int ca = 1;ca<=T;ca++){
        scanf("%d",&N);
        set<double> appear;
        appear.clear();
        for(int i=0;i<N;i++){
            cin >> num[i];

        }
        for(int i=0;i<N;i++){
            cin >> num2[i];
            appear.insert(num2[i]);
        }
        sort(num,num+N);
        sort(num2,num2+N);
        a1 = a2 = 0;
        int j=0;
        for(int i=0;i<N;i++){
            for(;j<N;){
                if(num2[j] > num[i]){
                    a2++;
                   // cout << num[i] << " " << num2[j]<<"\n";
                    j++;
                    break;
                }
                j++;
            }
            if(j == N)break;
        }

        int l,r;
        l = 0;
        r = N-1;
        for(int i=0;i<N;i++){
            if(num[i] > num2[l]){
                double now = num2[r];
                while(now <= 1.0 && appear.find(now) != appear.end())now += 0.00001;
                if(now > 1.0)break;
                a1++;
                appear.insert(now);
                l++;
            }else{
                r--;
            }
        }
        printf("Case #%d: %d %d\n",ca,a1,N-a2);
    }
    return 0;
}
/*
4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
*/
