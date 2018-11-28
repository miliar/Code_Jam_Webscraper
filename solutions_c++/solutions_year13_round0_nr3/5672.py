
#include <iostream>
#include <vector>

#define DEBUG(...) \
        fprintf(stdout,__VA_ARGS__)


using namespace std;

typedef struct {
    int key;
    int num;
    vector<int> kvector;
} Chests;

class FairAndSquare {

        int A; 
        int B;
        FILE * fip;
        FILE * fop;

    public:
        FairAndSquare(char * file) { 
                fip = fopen(file,"r");
                fop = fopen("./output.txt","w");
                if (!fop || !fip) {
                        cerr << "Cannot open input/output file.!";
                        exit(1);
                }
        }

        void Read();
        int  Process();
        int isSquare(int);
        bool isPalindrome(int);

        ~FairAndSquare() 
        { 
                if (fip) fclose(fip);
                fip = NULL;
                if (fop) fclose(fop);
                fop = NULL;
        }

};

void FairAndSquare::Read() {
        int T = 0,res = 0;
        fscanf(fip,"%d\n",&T);
        DEBUG("Number of tests : %d\n",T);
        for (int t = 0; t < T; t++) {
             fscanf(fip,"%d ",&A);
             fscanf(fip,"%d\n",&B);
             DEBUG("Start : %d end : %d\n",A,B);
             res = Process();
             fprintf(fop,"Case #%d : %d\n",t+1,res);
             DEBUG("Case #%d : %d\n",t+1,res);
        }
}  

vector<int> * vectorize(int num) {
    vector<int> * vec = new vector<int>;
    while  (num) {
      vec->push_back(num%10);
      num = num/10;
    }
    return vec;
}


bool FairAndSquare::isPalindrome(int num) {
   vector<int> * vec = vectorize(num);
   int len = vec->size();
   int s2,e1,i,j; 
   if (len == 1) {
     s2 = e1 = 0;
   }
   else if (len%2) {
      s2 = (len/2)+1;
      e1 = (len/2)-1;
   } else {
      s2 = len/2;
      e1 = len/2-1;
   }
   for(i=e1,j=s2;i>=0,j<len;i--,j++) 
       if(vec->at(i) != vec->at(j))
             return false;

   if (i== -1 && j == len)    
         return true;
    return false;

}

int FairAndSquare::isSquare(int num) {
   if ( num < 2)
      return 1;

   for(int i = 1  ; i <= num/2; i++)
     if ( i*i == num)
        return i;

   return 12;
}



int FairAndSquare::Process() {
      int ctr = 0;
      if ( A > B)
        return ctr;

      for(int i=A ; i <= B ; i++) {
          if (isPalindrome(i) && isPalindrome(isSquare(i)))
            ctr++;
      }       
      return ctr;
}


int main (int argc,char *argv[]) {
        if (argc > 2) {
                fprintf(stderr,"Incorrect number of arguments.\n");
                exit(1);
        }

        FairAndSquare obj(argv[1]);
        obj.Read();
}














