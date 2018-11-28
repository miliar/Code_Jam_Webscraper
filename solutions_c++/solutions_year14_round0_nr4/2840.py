#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void main(){

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t=0,n=0;
	scanf("%d",&t);
	//printf("%d\n",t);//test case
	for(int k=1;k<=t;k++){
	scanf("%d",&n);
	//printf("\n\n%d",n);
	vector<float> naomi(n),ken(n),naomip(n),kenp(n),naomig(n),keng(n);
//	printf("\n naomi");
	for(int k1=0;k1<n;k1++){
		scanf("%f",&naomi.at(k1));
	//	printf(" %.2f ",naomi[k1]);
	}
//	printf("\n ken");
	for(int k1=0;k1<n;k1++){
		scanf("%f",&ken.at(k1));
	//	printf(" %.2f ",ken[k1]);
	}
	sort(naomi.begin(),naomi.begin()+n);
	sort(ken.begin(),ken.begin()+n);
	naomip=naomi;
	kenp=ken;
//	printf("\n naomi");
	for(int k1=0;k1<n;k1++){
		//scanf("%f",&naomi.at(k1));
	//	printf(" %.3f ",naomip[k1]);
	}
//	printf("\n ken");
	for(int k1=0;k1<n;k1++){
		//scanf("%f",&naomi.at(k1));
//		printf(" %.3f ",kenp[k1]);
	}
	//Ken strategy all blocks
	//start from maximum
	int kenpnts=0;
	int nd=n-1;
	for(int k2=nd;k2>=0;k2--){
		for(int k3=0;k3<=nd;k3++){
		
		if(naomi[k2]<ken[k3]){
		
	//		cout<<"\nNaomi gets shot\n"<<naomi[k2]<<"Ken is"<<ken[k3];
			naomi.erase(naomi.begin()+k2);
			ken.erase(ken.begin()+k3);
			nd--;
	//		cout<<"\nNaomi   Ken\n";
			for(int chk=0;chk<=nd;chk++){
		//	cout<<naomi[chk]<<"  "<<ken[chk]<<"\n";
			}


			break;
		}
		
		
		}	
	}

	naomig=naomip;
	keng=kenp;
	//cout<<"Case #"<<k<<": "<<naomi.size()<<"\n";
	nd=n-1;
	int npts=0;

	while(nd>=0){
	if(naomig[nd]>keng[nd]){
	npts++;
	naomig.erase(naomig.begin()+nd);
	keng.erase(keng.begin()+nd);
	}else{
	naomig.erase(naomig.begin());
	keng.erase(keng.begin()+nd);
	
	}
	nd--;	
	}

	


	cout<<"Case #"<<k<<": "<<npts<<" "<<naomi.size()<<"\n";






	}

}