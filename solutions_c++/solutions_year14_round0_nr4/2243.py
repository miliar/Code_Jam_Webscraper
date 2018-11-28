			 #include<fstream.h>
			 #include<iomanip.h>
			 float v1[1000],v2[1000];
			 void sort(float [], int);
			 void main()
			 {          ifstream fin;
			 ofstream fout;
			 fout.open("out.txt") ;
			 int T,k,n,s1,s2,l1,l2,p1,p2,i,j,f,l;


  fin.open ("in.txt");
		fin>>T;

		for( k=1; k<=T; k++)
		{   fout<<"Case #"<<k<<": ";
			 fin>>n;
			 for(i=0;i<n;i++)
			 {fin>>v1[i];}
			 for(i=0;i<n;i++)
			 {fin>>v2[i];}
			sort(v1,n);
			sort(v2,n);
			s1=s2=p1=p2=0;
			l1=l2=n-1;
			for(i=0;i<n;i++)
			{
				 if(v1[l1]>v2[l2])
				 {
					p2++;
					s2++;
					l1--;
				 }
				 else
				 {l2--;
				 l1--; }
			}
			s1=s2=0;
			 l1=l2=n-1;
			for(i=0;i<n;i++)
			{  f=0;
				if(i+1==n)
				{
					if(v1[0]>v2[i])
					{p1++;}
				}
				else
				{   	for(j=0;j<=l1;j++)
						{
							if(v2[i]<v1[j])
							{  p1++;
								f=1;
								for(l=j;l<l1;l++)
								{v1[l]=v1[l+1] ;}
								break;
							}

						}

					l1--;
				}

			}
			fout<<p1<<" "<<p2<<endl;
		}
  fin.close();
  fout.close();
}
void sort(float v[],int n)
{
	int i,j;
	float t;
	for(i=0;i<n-1;i++)
	{
		j=0;
		while(j<n-i-1)
		{
			if(v[j]>v[j+1])
			{
				t=v[j];
				v[j]=v[j+1];
				v[j+1]=t;
			}
			j++;
		}
	 }
}