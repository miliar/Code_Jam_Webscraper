#include <fstream> // You should include this library
#include <iostream>
using namespace std;

int arr[7];
int arr2[7];
int main()
{
     freopen("B-large.in","r",stdin); // For reading input
     freopen("output2.txt","w",stdout); // for writing output
     int t;
     cin >> t;
     cout.precision(7);
     cout.setf( std::ios::fixed, std:: ios::floatfield );
     for (int i = 0; i < t; i++) {
    	 double c,f,x;
    	 cin >> c >> f >> x;
    	 double cnt = 2.0;
    	 double prev_best = x/cnt;
    	 double next_cnt;
    	 double best;
    	 double init_time = 0;
    	 while (true) {
    		 next_cnt = cnt+f;
    		 init_time += c/cnt;
    		 best = x/next_cnt + init_time;
    		 if (best >= prev_best) {
    			 break;
    		 }
    		 cnt = next_cnt;
    		 prev_best = best;
    	 }
    	 cout << "Case #" << i+1 << ": ";
    	 cout << prev_best;
    	 cout << endl;
     }
     return 0;
}
