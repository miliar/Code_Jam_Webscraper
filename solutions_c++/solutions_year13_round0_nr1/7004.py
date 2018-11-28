#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<string> inp(4,"....");
	int attempts =0;
	cin >> attempts;
	for ( int c=0;c<attempts;c++){
		vector<int> xrows(4,0);
		vector<int> xcolumns(4,0);
		vector<int> yrows(4,0);
		vector<int> ycolumns(4,0);
		int trow=-1;
		int tcol=-1;
		int xdiag=0,ydiag=0,y1diag=0,flag1=0,x1diag=0,tdiag=-1,t1diag=-1,flag=0;
		cin >> inp[0];
		cin >> inp[1];
		cin >> inp[2];
		cin >> inp[3];

		for(int j=0;j<inp.size();j++){
			for(int k=0;k<inp[j].size();k++){
				if(inp[j][k]=='X'){
					xrows[j]++;
					xcolumns[k]++;
					if(j==k) {
						xdiag++;
					}
					if (j+k ==3) x1diag++;
					flag++;
				}else if (inp[j][k]=='T') {
					trow=j;
					flag++;
					tcol=k;
					if (j==k) tdiag=1;
					if (j+k ==3) t1diag = 1;
				}else if (inp[j][k]=='O') {
					yrows[j]++;
                                        ycolumns[k]++;
                                        if(j==k) {
                                                ydiag++;
                                        }
                                        if (j+k ==3) y1diag++;
                                        flag++;
				}	
			}
		}
		for (int i=0;i<4;i++){
			if (xrows[i]==4 || xcolumns[i]==4 || xdiag==4 || x1diag ==4 || (xdiag==3 && tdiag==1) || (x1diag==3 && t1diag==1)) {
				printf("Case #%d: X won\n",c+1);
				flag1=1;
				break;
			}
		}
		if (flag1==1)continue;

		for (int i=0;i<4;i++){
			if (yrows[i]==4 || ycolumns[i]==4 || ydiag==4 || y1diag ==4 || (ydiag==3 && tdiag==1) || (y1diag==3 && t1diag==1)) {
				printf("Case #%d: O won\n",c+1);
				flag1=1;
				break;
			}
		}
		if (flag1==1)continue;

		if ( tcol > -1 && trow> -1){
			if (xrows[trow] == 3 || xcolumns[tcol]==3) {
			printf("Case #%d: X won\n",c+1);
			continue;
		}else if (yrows[trow]==3 || ycolumns[tcol]==3) {
			printf("Case #%d: O won\n",c+1);
			continue;
		}
}
		
		if (flag!=16) {
			printf("Case #%d: Game has not completed\n",c+1);
			continue;
		}
		printf("Case #%d: Draw\n",c+1);	
	}
	return 0;
} 
