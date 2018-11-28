#include<cstdio>

using namespace std;

int TC;
double C,F,X,total,temp,temp2;
double speed;
int a,status,counter=0;

double Hitung(float F)
 {
 	temp2 = total; // Tampung Sementara
 	
    total += (X / (F/10)) / 10;  // For Continuosly
 	if(temp < total) status = 1;
 	/*else
 	{
 		total = temp2;
 	}
 	*/
 	
 	/* Debugging
 	//printf("Total : %.7lf \t temp : %.7lf\n",total,temp);
 	//counter++;
 	*/
 	
 	return total;
 }

int main()
 {
	scanf("%d",&TC);
	for(a = 1; a <= TC; a++)
	{
		// Refresher
		status = 0;
		total = 0;
		speed = 2;
		temp2 = 0;
		
		scanf("%lf %lf %lf",&C,&F,&X);
		
		temp = (X / 0.2)  / 10;    // For the Continuosly 
		// Ketika masih untung untuk Terus melakukan Pembelian sawah
		while(status == 0)
		{
			total = temp2;
			total += (C / (speed / 10)) / 10;    
			speed = speed + F;
			total = Hitung(speed);
			if(status == 1) break;
			temp = total;
		}
		printf("Case #%d: %.7lf\n",a,temp);
	}
	
 	return 0;
 }
