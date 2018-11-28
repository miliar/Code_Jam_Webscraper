#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
   int t;
   scanf("%d", &t);
   int c = 0;
   while(t--)
   {
       int n = 0;
       scanf("%d", &n);

       double val = 0.0;
       vector<double> no;
       for (int i = 0; i < n; i++) {
            scanf("%lf", &val);
            no.push_back(val);
        }
        val = 0.0;
       vector<double> ken;
       for (int i = 0; i < n; i++) {
            scanf("%lf", &val);
            ken.push_back(val);
        }

        sort(no.begin(), no.end());
        sort(ken.begin(), ken.end());
        //sort(no.begin(), no.end());
        //sort(ken.begin(), ken.end());
        int win = 0;
        int i = 0;
        int j = n - 1;
        //int last = n - 1;
        for (i = n - 1; i >= 0; i--) {
        //	cout << no[i] << " " << ken[j] << endl;
             if (no[i] > ken[j]) {
          //        last--;
                  win++;

            } else if (no[i] < ken[j]) {
                 j--;

            }
        }
        int win1 = 0;
         i = 0;
         j = 0;
        for ( i = 0; i < n; i++) {
            //cout << no[i] << " " << ken[j] << endl;
            if (no[i] < ken[j]) {
                //i++;
            }else if (no[i] > ken[j]) {
              win1++;
              j++;
            }
        }
            //int answar = 0;
        //if (win == n)
          //answar = win;
          c++;
        printf("Case #%d: %d %d\n",c, win1, win);
        //if (no[i] < ken[1])



   }


}
