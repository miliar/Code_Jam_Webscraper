#include<iostream>
#include<fstream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test, temp = 0;
    cin >> test;
    for(int case1=1; case1<=test; case1++) {
        int n;
        double arr1[2022],arr2[2020];
        cin >> n;
        for(int i=0; i<n; i++)
            cin >> arr1[i];
        for(int j=0; j<n; j++)
            cin >> arr2[j];
        cout << "Case #" << case1 << ": ";
        sort(arr1,arr1+n), sort(arr2,arr2+n);
        int first_val = 0,sec_val = 0, ans4;
        for(int i = 0; i < n; i++) {
            first_val += (arr1[n-1] < arr2[i]);
            ans4 += first_val, temp = ans4;
        }
        sec_val = first_val;
        ans4 = first_val + sec_val;
        for(int i=sec_val; i<n; i++) {
            if(arr2[0] > arr1[i])
                sec_val++;
            ans4 += 1;
            temp = ans4;
        }
        int third_val = 0;
        int i = 0;
        while(sec_val < n) {
            if(arr2[i] < arr1[sec_val]) {
                i++, sec_val++, third_val++, ans4 += (third_val - sec_val);
            } else {
                sec_val++, ans4 += 2;
            }
        }
        int taken[2014] = {0};
        first_val = sec_val = 0;
        for(int i=0; i<2011; i++)
            taken[i] = 0;
        for(int i=0; i<n; i++) {
            bool f = 0;
            for(int j=0; j<n; j++) {
                if(taken[j] == 0 && arr1[i] < arr2[j]) {
                    taken[j] = 1, first_val++, f = 1;
                    break;
                }
            }
            if(!f) {
                for(int j=0; j<n; j++) {
                    if(taken[j] == 0) {
                        taken[j] = 1;
                        break;
                    }
                }
            }
        }
        sec_val = n-first_val;
        cout << third_val << " " << sec_val << endl;
    }
}
