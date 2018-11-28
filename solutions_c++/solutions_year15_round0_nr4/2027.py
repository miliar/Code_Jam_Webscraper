#include <vector>
#include <algorithm>
#include <fstream>
#include <stdlib.h> 
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stack>
#include <string.h>
#include <iomanip>
#include <sstream>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int i, numCase;
	cin>>numCase;
	int x, r, c;
	for(i=0; i<numCase; i++){
		bool gabe=false, richard=false;
		cin>>x>>r>>c;
		if(x > r*c){
			richard=true;
		}
		else{
			if(x==1){
				gabe=true;
			}
			else if(x==2){
				if((r*c)%2){
					richard=true;
				}
				else{
					gabe=true;
				}
			}
			else if(x==3){
				if((r*c)%3){
					richard=true;
				}
				else{
					if(r==1 || c==1){
						richard=true;
					}
					else{
						gabe=true;
					}
				}
			}
			else if(x==4){
				if((r*c)%4){
					richard=true;
				}
				else{
					if(r<=2 || c<=2){
						richard=true;
					}
					else{
						gabe=true;
					}
				}
			}
		}
		if(gabe){
			cout << "Case #" << (i+1) << ": Gabriel"<<endl;
		}
		else{
			cout << "Case #" << (i+1) << ": Richard"<<endl;
		}
	}
    return 0;
}
