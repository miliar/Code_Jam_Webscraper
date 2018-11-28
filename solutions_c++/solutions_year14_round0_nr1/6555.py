#include <iostream>
#include <set>
using namespace std;

int main()
{
	printf("aa\n");
	int iCase=0;
	int iRow=0;
	int arr[4];
	set<int> iSet;
	cin>>iCase;
	string *s = new string[iCase];
	char ch[100];
	for(int i=0;i<iCase;++i){
		bool bFlag = false;
		int iAns=-1;
		iSet.clear();
		cout<<"aa"<<endl;
		for(int t=0;t<2;++t){
			cin>>iRow;
			for(int j=1;j<=4;++j){
				scanf("%d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3]);
				if (iRow == j){
					if (t == 0){
						for(int k=0;k<4;++k){
							iSet.insert(arr[k]);
						}
					}else{
						for(int k=0;k<4;++k){
							if (iSet.find(arr[k]) != iSet.end()){
								if (bFlag == false){
									bFlag = true;
									iAns = arr[k];
								}else{
									sprintf(ch, "Case #%d: Bad magician!\n", i+1);
									s[i]=ch;
									iAns = -1;
								}
							}
						}
						if (bFlag == false){
							sprintf(ch, "Case #%d: Volunteer cheated!\n", i+1);
							s[i]=ch;
						}else if (iAns != -1){
							sprintf(ch, "Case #%d: %d\n", i+1, iAns);
							s[i]=ch;
						}
					}
				}
			}
		}
	}
	for(int i=0;i<iCase;++i){
		cout<<s[i].c_str();
	}
	
	return 0;
}