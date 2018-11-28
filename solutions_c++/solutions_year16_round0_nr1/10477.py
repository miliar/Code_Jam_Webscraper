#include <iostream>
using namespace std;

main()
{
	FILE *fp,*ft;
	int total, collection[10], mod;
	int count=0, local;
	ft = fopen("A-large.in.txt","r");
	fp = fopen("Output1.txt","w");
	if(ft != NULL)
		{
		fscanf(ft,"%d", &total) ;
		if(total>=1 && total <=100)
		{
			int select[total];
			for(int i=0 ; i<total; i++)
			fscanf(ft,"%d",&select[i]);
			for(int i=0 ; i<total ; i++)
			{
				fprintf(fp,"Case #%d", i+1 );
				fprintf(fp,": ");
				
				if(select[i] >= 0 && select[i] <=1000000)
				{
					if(select[i] == 0)
					fprintf(fp,"INSOMNIA\n");
					else
					{
						int statloc=1;
						local = select[i];
						for(int j=0 ; j<10; j++)
						collection[j] = 100;
						while(count != 45)
						{
							count=0;
							select[i] = local * statloc++;
							int local1=select[i];
			 				while(local1 != 0)
							{
								mod=local1%10;
								collection[mod] = mod;
								local1/=10;
							}
							for(int i=0; i<10; i++)
							count += collection[i];
						}
						count=0;
						fprintf(fp,"%d\n", select[i] );
					}
				}
					else
					fprintf(fp, "Large DataSet Number...\n") ;
			}	
		}
		else
		fprintf(fp,"Your Limit is exceeded...\n");
		fclose(fp);
		fclose(ft);
	}
	else
	cout << "There is No Such File" << endl;
	cout << "Program Ended Successfully..." ;
}
