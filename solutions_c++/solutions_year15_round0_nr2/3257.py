//
//  main.cpp
//  infinite house of pancakes
//
//  Created by Estelle :) on 11/4/15.
//  Copyright (c) 2015 AWESOMENESS. All rights reserved.
//

#include <iostream>
#include <queue>
using namespace std;
int arr[1005];
int d;

int main() {
    int t;
    freopen("/Users/student/Downloads/B-large.in", "r", stdin);
    scanf("%d", &t);
    for (int i=0; i<t; i++) {
        scanf("%d", &d);
        int m=0;
        for (int j=0; j<d; j++) {scanf("%d", &arr[j]); m=max(m,arr[j]);}
        int l=0;
        int h=m;
        int ans;
        while (h-l>=0) {
            
            int mid=(h-l)/2+l;
            bool s=false;
            for (int j=0; j<mid; j++) {
                int p=j;
                for (int k=0; k<d; k++) {
                    if (arr[k]>mid-j) {
                        p-=(arr[k]/(mid-j)-1);
                        if (arr[k]%(mid-j)!=0) p--;
                    }
                }
                if (p>=0) {
                    s=true;
                    break;
                }
            }
            if (h-l==1) {
                if (s) ans=l;
                else ans=h;
                break;
            }
            else if (h-l==0) {
                if (s) ans=l;
                break;
            }
            if (s) {
                h=mid;
            }
            else l=mid+1;
            
        }
        printf("Case #%d: %d\n", i+1, ans);
    }
}
