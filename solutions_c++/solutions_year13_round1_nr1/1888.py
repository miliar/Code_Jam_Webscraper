#include<fstream>

using namespace std;

const char* input_fname = "input";
const char* output_fname = "output";


int main(void)
{
    ifstream in(input_fname);
    ofstream out(output_fname);

    int testcase_sz = 0;
    in >> testcase_sz;

    for(int case_id=1;case_id<=testcase_sz;case_id++)
    {
        long long r,t;
        in >> r >> t;

        t -= 2*r+1;
        int ans = 1;

        while(t>0)
        {
            t -= 2*(r+2*ans)+1;
            if(t>=0) ans++;
        }


        out << "Case #" << case_id << ": " << ans;

        if(case_id<testcase_sz) out << endl;
    }

    return 0;
}
