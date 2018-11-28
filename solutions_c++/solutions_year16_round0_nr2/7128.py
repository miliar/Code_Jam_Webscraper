//Design By Robert Jiun-Ting Jiang 20160409
//gcj2016_qualify_pb__翻翻stack 
//Dev-C++
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>

//#include <fstream>

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

int FStack[100+1]; //放入+表示1，-表示0 
int n_FStack=0;
//ifstream fin("in.txt"); 


//寫一個翻翻Stack的函數 由最左第一個 到指定的第n個翻一趟

int  flipFStack(int n) { 
	//0換為1,  
	int t;		
	/*if (n%2 != 0) { 
		//FStack[n/2+1] = ZeroOneSwap(FStack[n/2+1]); //^1;
		FStack[n/2+1]^1;
	}
	for (int i=1 ; i<=n/2;i++){
		//t=ZeroOneSwap(FStack[i] ); FStack[i]=ZeroOneSwap(FStack[n-i+1]);  FStack[n-i+1]=t;
		t=FStack[i]^1; FStack[i]=FStack[n-i+1]^1;  FStack[n-i+1]=t;}
	*/
	for (int i=1 ; i<=n;i++){
		FStack[i]^=1;
	}
	for (int i=1 ; i<=n/2;i++){		
		t=FStack[i]; FStack[i]=FStack[n-i+1];  FStack[n-i+1]=t;
	}	
	return 0;
}

int main() {
  
    int n_testcase, i, j, x, y;

    cin >> n_testcase;    
    for ( int i_testcase=1; i_testcase<=n_testcase;i_testcase++)  {        
        cout << "Case #" << (i_testcase) << ": ";
		string ss_in;
        cin >> ss_in;

        int ii;
        for (int i=1;i<=ss_in.length(); i++){
			FStack[i]=(ss_in.substr(i-1,1)=="-"?0:1);
			ii=i;
		}
		//FStack[ii+1]=999;
		//分為四類：如果待處理區域為1..i 則 
		//case  0 0,  0 1,  1 0,   1,1
		
		//若未尾為1表示已正確。就由 1..i改為 1..(i-1)
		//若未尾不為1表示0, 要由第1個來換，若
		//              若 第1個剛好是0，則翻過來後，就把未尾變為1，
		//              若 第1個卻是1，則要由尾巴 (i-1) ..(1)倒著找，直到有1再把那個1翻到最前變0，才可以再翻到未尾變為1
		
					
		n_FStack=0;
		//由末尾檢查 ，看是否要翻Stack並且記錄總共翻幾次。 
		for (int i=ss_in.length();i>=1; i--){
			if (FStack[i]==1) {
			} else { //0則要先看前面是0,1? 
			    //現在末尾的 [i]是0，所以要翻！ 
				if (FStack[1]==0){
					n_FStack++;
					flipFStack(i) ;
				} else {
					//要先讓第1個變為0，所以由末尾(i-1)往前找第一個1.
					int iTail=i-1;
					for (;iTail>=1; iTail--){
						if(FStack[iTail]==1)break; //最多就找到第一個的1 
					}
					n_FStack++;
					flipFStack(iTail);
					//此時第一個變為0了，所以可以直接翻，使未尾變1 
					flipFStack(i) ;
					n_FStack++;
				}
			}
		}
        cout << n_FStack << endl;
    }
    return 0;
}


