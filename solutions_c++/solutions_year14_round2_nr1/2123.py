#include <iostream>
#include <cstring>
#include <stdio.h>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    
	int arr[1000];
        int arr1[1000];
        int cost_min,len;
        int cost,temp;
        int ans;
    int i,j,k,n,t,z,p,m,h,r,e;
    cin>>t;
    int flag;
    for (j = 1 ; j <= t ; j++) {
        
		cin>>n;
		
        char ed[105][105];

        for (i = 0 ; i < n ; i++) {
            cin>>ed[i];
        }
       char ed2[105][105];
	          for (i = 0 ; i < n ; i++) {
            z = strlen(ed[i]);
             p = 0;
            for (k = 0 ; k < z ; k++) {
                	ed2[i][p] = ed[i][k];
                while(ed[i][k] == ed[i][k+1]) {
                    k++;
                }
                p++;
            }
            ed2[i][p] = '\0';
        } 

        flag = 0;
        for (i = 0 ; i < n-1 ; i++) {
            if (strcmp(ed2[i],ed2[i+1]) != 0) {
                flag = 1;
                break;
            }
        }

        if (flag == 1) {
            printf("Case #%d: Fegla Won\n",j);
            continue;
        }


         cost_min = 0;
        len = strlen(ed2[0]);
        for (i = 0 ; i < n ; i++) {
             temp = strlen(ed[i]) - len;
            cost_min = cost_min + abs(temp);
        }


        k = 0;
        for (i = 0; i < strlen(ed[0]); i++) {
            arr[k] = 1;
            while (ed[0][i] == ed[0][i+1]) {
                i++;
                arr[k]++;
            }
            k++;
        }
        k = 0;
        for (i = 0; i < strlen(ed[1]); i++) {
            arr1[k] = 1;
            while (ed[1][i] == ed[1][i+1]) {
                i++;
                arr1[k]++;
            }
            k++;
        }

         cost = 0;      for ( m = 0 ; m < k ;m++) {
            
             z = arr[m]-arr1[m];
            cost = cost + abs(z);
        }      
         ans = cost_min < cost ? cost_min : cost;
	printf("Case #%d: %d\n",j,ans);

    }
    return 0;
}

