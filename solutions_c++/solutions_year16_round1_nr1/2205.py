//Design By Robert Jiun-Ting Jiang 20160416
//gcj2016_round1A_pa
//Dev-C++
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <string>     // std::string, std::stoi

#include <iostream>   // std::cout
#include <string>     // std::string, std::stoi

//#include <deque>


/*用 fin , fout 的檔案輸出入取代 標準輸出入 
    #include <fstream>
    ifstream fin("in.txt");   
    ofstream fout("out.txt"); 
	// fin>>i;  fout<<"ddd";
*/
//轉換任意形態的資料，用stringstream轉為字串，例如數字為字串。 string(number) 
/*int  ans=987;
string ss = "";
stringstream ssm;
ssm.clear();ssm << ans ; ssm >> ss; 
ss = ss.substr(ss.length()-1,1); //印出最末個數字 
cout << ss << endl;
exit;
*/
using namespace std;

////////////////////////////////////////////////////////////////////////////////



int main() {

    #define MAX 1000+2
    char buffer[MAX];      
    
   
    int n_testcase, i, j, x, y;
	
	
    //cin >> n_testcase;     //若行輸入，則連第一個數字，就要用行輸入！ 
    
    cin.getline(buffer,MAX);
    stringstream ssm;
	ssm.clear();ssm << buffer ; ssm >> n_testcase; 	
	//string s_in; 
	
    for ( int i_testcase=1; i_testcase<=n_testcase;i_testcase++)  {        
        cout << "Case #" << (i_testcase) << ": ";		
        //cin >> s_in;
        string s_in;        
        cin.getline(buffer,MAX);
        stringstream ssm;
		ssm.clear();ssm << buffer ; ssm >> s_in;		   		
        string s_ans="";
        for (int le=0; le< s_in.length(); le ++){
        	string s_single=s_in.substr(le,1);
        	if (s_single>= s_ans.substr(0,1)){
        		s_ans=s_single+s_ans;
        	}else {
        		s_ans=s_ans+s_single;
			}			
		}
		cout << s_ans<<endl;	
    }
    return 0;
}

