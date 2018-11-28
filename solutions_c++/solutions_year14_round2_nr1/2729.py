#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
	int t,i,j,temp,z,g;
	char a[101],b[101];
	FILE *ifp,*ofp;
	ifp = fopen("A-small-attempt1.in","r");
	ofp = fopen("output1.in","w");
	fscanf(ifp,"%d",&t);
	//fprintf(ofp,"%d\n",t);
	for(int k=0;k<t;k++){
		i=0;
		j=0;
		temp=0;
		z=0;
		fscanf(ifp,"%d",&g);
		//fprintf(ofp,"%d\n",g);
		fscanf(ifp,"%s%s",a,b);
		while(a[i]!='\0' || b[j] != '\0'){
			// if((a[i]=='\0' && b[j]!='\0') ||(a[i] != '\0' && b[j] == '\0')){
			// 	z=1;
			// 	break;
			// }
			if(a[i]==b[j]){
				i++;
				j++;
			}
			else{
				if(a[i]==b[j-1]){
					i++;
					temp++;
				}
				else if(a[i-1]==b[j]){
					j++;
					temp++;
				}
				else{
					z=1;
					break;
				}
			}
		}
		if(z==0)
			fprintf(ofp,"Case #%d: %d\n",k+1,temp);
			//cout<<"Case #"<<k+1<<" :"<<temp<<endl;
		else
			fprintf(ofp,"Case #%d: Fegla Won\n",k+1);
			//cout<<"Case #"<<k+1<<" :"<<"Fegla Won"<<endl;
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}