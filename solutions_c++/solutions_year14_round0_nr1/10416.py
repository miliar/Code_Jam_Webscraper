#include<fstream>

using namespace std;

int main(int argc, char *argv[])
{

        ifstream fin(argv[1]);
        ofstream fout(argv[2]);

        int T; fin>>T;

        for(int cases = 1; cases<=T; cases++)
        {
                int r1, r2, A[4], B[4]; int temp;

                fin>>r1;
                for(int i=1;i<=4;i++)
                 	for(int j=0;j<4;j++)
                      	{
				if (i==r1)
					fin>>A[j];
				else
					fin>>temp;
			}

                fin>>r2;
                for(int i=1;i<=4;i++)
                        for(int j=0;j<4;j++)
                        {
				if(i==r2)
 					fin>>B[j];					
				else
					fin>>temp;
			}

                int count = 0; int num;
	
                for(int i=0;i<4;i++)
		{	
			for(int j=0;j<4;j++)
			{
                        	if(A[i] == B[j])
                        	{
                                	count++;
                                	num = A[i];
					break;
                        	}
			}

                        if(count>1)
                        {
                                //num = -1;
                                break;
                        }
                }

                fout<<"case #";
		fout<<cases;
                fout<<": ";
		string s = "";

                if(count == 0)
                        s = s+"Volunteer cheated!\n";
                else
                {
                        if(count>1)
                        s = s+"Bad magician!\n";
                        else
                        {
				fout<<num;
				s = "\n";			
			}
                }

                fout<<s;

        }

        fin.close(); 
	fout.close();

        return 1;
}


