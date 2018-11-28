#include <stdio.h>
#include <vector>
using namespace std;
main(){
	
	int ncases,a,b,temp,caso=1;
	scanf("%d",&ncases);
	int arr1[5],arr2[5];
	while(ncases--){
		scanf("%d",&a);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(i==a)
					scanf("%d",&arr1[j]);
				else
					scanf("%d",&temp);
			}
		}

		scanf("%d",&b);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(i==b)
					scanf("%d",&arr2[j]);
				else
					scanf("%d",&temp);
			}
		}

		vector <int> vec;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				if(arr1[i]==arr2[j])
					vec.push_back(arr1[i]);
			}
		}
		printf("Case #%d: ",caso);
		if(vec.size()==0)
			printf("Volunteer cheated!\n");
		else if(vec.size()>1)
			printf("Bad magician!\n");
		else if(vec.size()==1)
			printf("%d\n",vec[0]);

		caso++;

	}
}