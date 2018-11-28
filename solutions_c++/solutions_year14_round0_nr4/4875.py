#include <cstdio>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    FILE* fp;
    int i, j, k, T, number, count1, count2;
    vector<double> a, b;
    double temp;
    fp = fopen("kkk", "w");
    scanf("%d", &T);
    for(i = 0; i < T; i++){
        scanf("%d", &number);
        for(j = 0; j < number; j++){
            scanf("%lf", &temp);
            a.push_back(temp);
        }
        
        for(j = 0; j < number; j++){
            scanf("%lf", &temp);
            b.push_back(temp);
        }
        sort(a.begin(), a.begin()+number);
        sort(b.begin(), b.begin()+number);
        count1 = 0;
        for(j = number-1, k = number-1; j >= 0 && k>= 0; ){
            if(a[j] > b[k]){
                count1++;
                j--;
                k--;
            }
            if(a[j] < b[k])
                k--;
        }
        count2 = 0;
        for(j = number-1, k = number-1; j >= 0 && k>= 0; ){
            if(b[j] > a[k]){
                count2++;
                j--;
                k--;
            }
            if(b[j] < a[k])
                k--;
        }
        a.clear();
        b.clear();
        fprintf(fp,"Case #%d: %d %d\n",i+1, count1, number-count2);
    }
}
