#include<fstream>

using namespace std;

const char* input_fname = "input";
const char* output_fname = "output";

int lawn[100][100] = {100};
int N=0;
int M=0;

bool check(void);

int main(void)
{
    ifstream in(input_fname);
    ofstream out(output_fname);

    int testcase_sz = 0;
    in >> testcase_sz;

    for(int case_id=1;case_id<=testcase_sz;case_id++)
    {
        in >> N >> M;
        for(int n=0;n<N;n++)
        {
            for(int m=0;m<M;m++)
            {
                in >> lawn[n][m];
            }
        }

        if( check() ) out << "Case #" << case_id << ": YES";
        else out << "Case #" << case_id << ": NO";

        if(case_id<testcase_sz) out << endl;
    }

    return 0;
}

bool check(void)
{
    for(int n=0;n<N;n++)
    {
        for(int m=0;m<M;m++)
        {
            int height = lawn[n][m];
            int nn=0, mm=0;

            for(;nn<N;nn++)
            {
                if( height>=lawn[nn][m] ) continue;
                else
                {
                    break;
                }
            }
            if( nn==N ) continue;

            for(;mm<M;mm++)
            {
                if( height>=lawn[n][mm] ) continue;
                else break;
            }
            if( (mm==M) ) continue;

            return false;
        }
    }
    return true;
}
