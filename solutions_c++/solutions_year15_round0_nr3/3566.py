#include<iostream>
using namespace std;

string Exchange(string first, string second){
  //cout << "exchange:" <<first << "," << second << endl;

  if(first.compare(0,1,"1") == 0){
    if(second.compare(0,1,"i") == 0) return "i";
    if(second.compare(0,1,"j") == 0) return "j";
    if(second.compare(0,1,"k") == 0) return "k";
  }else if(first.compare(0,2,"-1") == 0){
    if(second.compare(0,1,"i") == 0) return "-i";
    if(second.compare(0,1,"j") == 0) return "-j";
    if(second.compare(0,1,"k") == 0) return "-k";
  }else if(first.compare(0,1,"i") == 0){
    if(second.compare(0,1,"i") == 0) return "-1";
    if(second.compare(0,1,"j") == 0) return "k";
    if(second.compare(0,1,"k") == 0) return "-j";    
  }else if(first.compare(0,2,"-i") == 0){
    if(second.compare(0,1,"i") == 0) return "1";
    if(second.compare(0,1,"j") == 0) return "-k";
    if(second.compare(0,1,"k") == 0) return "j";    
  }else if(first.compare(0,1,"j") == 0){
    if(second.compare(0,1,"i") == 0) return "-k";
    if(second.compare(0,1,"j") == 0) return "-1";
    if(second.compare(0,1,"k") == 0) return "i";    
  }else if(first.compare(0,2,"-j") == 0){
    if(second.compare(0,1,"i") == 0) return "k";
    if(second.compare(0,1,"j") == 0) return "1";
    if(second.compare(0,1,"k") == 0) return "-i";
  }else if(first.compare(0,1,"k") == 0){
    if(second.compare(0,1,"i") == 0) return "j";
    if(second.compare(0,1,"j") == 0) return "-i";
    if(second.compare(0,1,"k") == 0) return "-1";
  }else if(first.compare(0,2,"-k") == 0){
    if(second.compare(0,1,"i") == 0) return "-j";
    if(second.compare(0,1,"j") == 0) return "i";
    if(second.compare(0,1,"k") == 0) return "1";    
  }
}
		     
int main(){
  int T; int t=0;
  cin >> T;
  //cout << T << endl;

  while(t < T){
    int L,X;
    string input,stored; string judge="0";
    cin >> L >> X;
    //cout << L << "," << X << endl;
    cin >> input;

    for(int i=0; i<X; i++)
      stored += input;
    //cout << stored << ":" << endl;

    while(stored != "ijk" && stored.size() > 3){
      //cout << stored.size() << "," << stored << endl;
      
      if(stored.compare(0,1,"i") == 0){
	if(stored.compare(1,1,"j") == 0){
	  if(stored.compare(2,1,"k") == 0){
	    judge = stored.substr(3);
	    break;
	  }else if(stored.compare(2,1,"k") != 0){
	    if(stored.compare(2,1,"-") == 0)
	      stored = "ij" + Exchange(stored.substr(2,2),stored.substr(4,1)) + stored.substr(5);
	    else
	      stored = "ij" + Exchange(stored.substr(2,1),stored.substr(3,1)) + stored.substr(4);
	  }
	}else if(stored.compare(1,1,"j") != 0){
	  if(stored.compare(1,1,"-") == 0)
	    stored = "i" + Exchange(stored.substr(1,2),stored.substr(3,1)) + stored.substr(4);
	  else
	    stored = "i" + Exchange(stored.substr(1,1),stored.substr(2,1)) + stored.substr(3);
	}
      }else if(stored.compare(0,1,"i") != 0){
	if(stored.compare(0,1,"-") == 0)
	  stored = Exchange(stored.substr(0,2),stored.substr(2,1)) + stored.substr(3);
	else
	  stored = Exchange(stored.substr(0,1),stored.substr(1,1)) + stored.substr(2);	
      }
    }
    //cout << stored << "," << judge << endl;

    while(judge != "0" && judge.size() > 1){
      //cout << judge << endl;
      if(judge.compare(0,1,"-") == 0){
	if(judge.size() <= 2) break;
	judge = Exchange(judge.substr(0,2),judge.substr(2,1)) + judge.substr(3);
      }else{
	judge = Exchange(judge.substr(0,1),judge.substr(1,1)) + judge.substr(2);	      
      }
    }
    //cout << stored << "," << judge << endl;

    if(judge != "0"){
      stored = stored.substr(0,3);
      //cout << stored << endl;
      stored = "ij" + Exchange(judge,stored.substr(2,1));
    }
    //cout << stored << endl;

    if(stored == "ijk") cout << "Case #" << t+1 << ": YES" << endl;
    else cout << "Case #" << t+1 << ": NO" << endl;

    t++;
  }
}
