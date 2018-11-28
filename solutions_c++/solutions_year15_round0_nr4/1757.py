#include <cstdio>
#include <iostream>
using namespace std;

int main(){
	freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int casos, i,a,b,c;
    cin >> casos;
    for(i=1;i<=casos;i++){
    	cin >> a >> b >> c;
    	if(a==4){
    		if((b==3 && c==4) || (b==4 && c==3) || (b==4 && c==4)){
				cout << "Case #" << i << ": GABRIEL\n";
    		}else{
    			cout << "Case #" << i << ": RICHARD\n";
    		}
    	}else if(a==3){
    		if((b==2 && c==3) || (b==3 && c==2) || (b==3 && c==4) || (b==4 && c==3) || (b==3 && c==3)){
    			cout << "Case #" << i << ": GABRIEL\n";
    		}else{
    			cout << "Case #" << i << ": RICHARD\n";
    		}
    	}else if(a==2){
    		if((b==1 && c==1) || (b==1 && c==3) || (b==3 && c==1) || (b==3 && c==3)){
    			cout << "Case #" << i << ": RICHARD\n";
    		}else{
    			cout << "Case #" << i << ": GABRIEL\n";
    		}
    	}else if(a==1){
    		cout << "Case #" << i << ": GABRIEL\n";
    	}
    }
    return 0;
}