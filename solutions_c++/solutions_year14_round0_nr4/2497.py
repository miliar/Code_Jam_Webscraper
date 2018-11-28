#include "iostream"
#include "cstring"
#include "cstdio"
#include "algorithm"
using namespace std;
#define read	 freopen("C:\\Users\\XPX\\Desktop\\D-large.in","r",stdin)
#define write	 freopen("C:\\Users\\XPX\\Desktop\\outDD.txt","w",stdout)

int n;
double a[1024];
double b[1024];

int main() {
        //read;
        //write;
	int T, cas = 0;
        cin >>T;
        while (T--) {
                cin >> n;
                for (int i = 0; i < n; i++) {
                        cin >> a[i];
                }
                for (int i = 0; i < n; i++) {
                        cin >> b[i];
                }
                sort (a, a + n);
                sort (b, b + n);
                int i = 0 , j = 0;
                int s1 = 0 , s2 = 0;
                while (i < n && j < n) {
                        if (a[i] < b[j]) {
                                i ++;
                        }else {
                                s1 ++;
                                i ++;
                                j ++;

                        }
                }

                i = 0; j = 0;
                while (i < n && j < n) {
                        if (b[j] > a[i]) {
                                i ++;
                                j ++;
                        }else {
                                s2 ++ ;
                                j ++ ;
                        }
                }
                printf("Case #%d: %d %d\n",++cas , s1, s2);
        }
	return 0;
}
