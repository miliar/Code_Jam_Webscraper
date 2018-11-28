#include<iostream>
int main()
{
  int mat1[4][4],mat2[4][4],t,r1,r2;
  std::cin>>t;
  for(int k=1;k<=t;++k)
  {
    std::cin>>r1;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
	std::cin>>mat1[i][j];
    std::cin>>r2;
    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
	std::cin>>mat2[i][j];
    int count=0,pos;
    for(int i=0;i<4;++i)
    {
      for(int j=0;j<4;++j)
      {
	if(mat1[r1-1][i]==mat2[r2-1][j])
	{
	  count++;
	  pos=i;
	}
      }
    }
    if(count==1)
      std::cout<<"Case #"<<k<<": "<<mat1[r1-1][pos]<<"\n";
    else if(count>1)
      std::cout<<"Case #"<<k<<": Bad magician!\n";
    else if(count==0)
      std::cout<<"Case #"<<k<<": Volunteer cheated!\n";
  }
}