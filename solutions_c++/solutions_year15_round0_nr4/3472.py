#include <algorithm>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_set>
#include <vector>


using namespace std;


int solution_war()
{
    //freopen("input.txt","r",stdin);
    ifstream fis("D-small-practice.in");
    //ofstream fos("output.txt");
    //freopen("D-small-practice-mine.out","w",stdout);
    
    
    int caseNum = 0;
    int T = 0;
    fis >> T;
    
    while (T--) {
        int B; fis >> B;
        
        vector<float> niomi;
        vector<float> ken;
        
        for (int i= 0; i < B; i++) {
            float b; fis >> b;
            niomi.push_back(b);
        }
        sort(niomi.begin(), niomi.end(), greater<float>());
        
        for (float a : niomi) {
            std::cout << a << " ";
        }
        cout << endl;
        
        for (int i= 0; i < B; i++) {
            float b; fis >> b;
            ken.push_back(b);
        }
        sort(ken.begin(), ken.end(), greater<float>());
        
        for (float a : ken) {
            std::cout << a << " ";
        }
        cout << endl;
        
        int z = 0;
        int hi = 0, lo =B-1;
        for (int i= 0; i < B; i++) {
            if (niomi[i] > ken[hi]) {
                z++;
                lo--;
            } else {
                hi++;
            }
        }
        
        int y = 0;
        hi = 0, lo =B-1;
        for (int i= B-1; i >= 0; i--) {
            if (niomi[i] < ken[hi]) {
                hi++;
            } else {
                y = B - hi;
            }
        }
        
        
        //fos << "Case #" << ++caseNum << ": " << y << " " << z << endl;
        cout << "Case #" << ++caseNum << ": " << y << " " << z << "\n";
    }
    
    return 0;
}



int main(int argc, const char * argv[])
{
    
    return solution_war();
    
    
    freopen("D-small-practice.in","r",stdin);
    //freopen("input","r",stdin);
    //freopen("B-small-attempt1.in.txt","r",stdin);
    //ofstream fos("D-small-practice.out");
    freopen("D-small-practice.out","w",stdout);
    
    int cas, n, ans[2], r;
    double a[2][1010];
    scanf("%d", &cas);
    for (int ii=0; ii<cas; ii++) {
        scanf("%d", &n);
        for(int i=0; i<2; i++) {
            for(int j=0; j<n; j++) {
                scanf("%lf", &a[i][j]);
            }
        }
        
        std::sort(a[0], a[0]+n);
        std::sort(a[1], a[1]+n);
        
        for(int i=0; i<2; i++) {
            r = 0;
            for (ans[i]=0; ans[i]<n; ans[i]++, r++) {
                while (a[i][ans[i]] > a[1-i][r] && r < n) {
                    r++;
                    if (r == n) break;
                }
            }
        }
        printf("Case #%d: %d %d\n", ii+1, ans[1], n-ans[0]);
    }
    
    return 0;
}


