//Design By Robert Jiun-Ting Jiang 20160416
//gcj2016_round1A_pb
//Dev-C++
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <string>     // std::string, std::stoi
#include <algorithm>

#include <iostream>   // std::cout
#include <string>     // std::string, std::stoi



//#include <deque>


/*ノ fin , fout 郎块 夹非块 
    #include <fstream>
    ifstream fin("in.txt");   
    ofstream fout("out.txt"); 
	// fin>>i;  fout<<"ddd";
*/
//锣传ヴ種篈戈ノstringstream锣﹃ㄒ计﹃ string(number) 
/*int  ans=987;
string ss = "";
stringstream ssm;
ssm.clear();ssm << ans ; ssm >> ss; 
ss = ss.substr(ss.length()-1,1); //程ソ计 
cout << ss << endl;
exit;
*/
using namespace std;

////////////////////////////////////////////////////////////////////////////////

int main() {
    
    int n_testcase, i, j, x, y;
    cin >> n_testcase;     //璝︽块玥硈材计碞璶ノ︽块 

    for ( int i_testcase=1; i_testcase<=n_testcase;i_testcase++)  {        
        cout << "Case #" << (i_testcase) << ": ";		
        #define HEIGHT_MAX 2500
        int Hash[HEIGHT_MAX+1] ; //Hash 计 
		for (int j=0;j<=HEIGHT_MAX; j++){
			Hash[j]=0;
		}
		int n_num; 
		cin >> n_num;
		#define N_MAX 50
		int x_in[N_MAX*2-1][N_MAX]; 		
		for (int i_n_num=0;i_n_num< 2*n_num-1 ; i_n_num++)	{
			for (int j_n_num=0; j_n_num< n_num ; j_n_num++) {
				int x;
				cin >> x; 
				Hash[x]++;
				x_in[i_n_num][j_n_num]=x;				
			}
		}
		//т计计N计
		int odd_ar[N_MAX];		
		int n_odd_ar=0;
		for (int i=0;i<=HEIGHT_MAX;i++){
			if ( Hash[i]%2 != 0)  odd_ar[n_odd_ar++]=i; //cout << "计计" << i << endl;
		}		
		//int x_end=sizeof(x)/sizeof(int);
		sort(odd_ar,odd_ar+n_num-1);
		
		for (int i_n_num=0;i_n_num< n_num ; i_n_num++)	{
			cout << odd_ar[i_n_num] << " ";
		}
		cout << endl;
    }
    return 0;
}

