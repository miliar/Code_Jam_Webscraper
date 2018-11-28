#include "mylib.h"


xint one_sheep_go(xint data_in) {
  if (0>=data_in) return 0;
  int curr_bits=0;
  xint curr_value=data_in;
  for (int k=1; k<1000000; k++) {
    // set bits from curr_value
    xint v=curr_value;
    while (0<v) {
      int last=v%10;
      curr_bits|=(1<<last);
      v/=10;
    }
    // check if all bits are one
    if (curr_bits==0x3ff) return curr_value;
    curr_value+=data_in;
  }
  // suppose 1000000 times is enough
  return 0;
}

void one_sheep(ccharp path_in, ccharp infile_in, ccharp outfile_in) {
  mifstream infile(path_in, infile_in);
  mofstream outfile(path_in, outfile_in);
  int count=0;
  if (!(infile>>count)) throw "count missing";
  cout<<"count= "<<count<<endl;
  for (int i=1; i<=count; i++) {
    xint data=-1;
    infile>>data;
    if (0>data) {
      throw "negative indata";
    }
    xint result=one_sheep_go(data);
    if (0<result) {
      xint times=result/data;
      cout<<"Case #"<<i<<": "<<result<<"="<<data<<"*"<<times<<endl;
    }
    ostringstream res;
    if (0==result) res<<"INSOMNIA";
    else res<<result;
    outfile<<"Case #"<<i<<": "<<res.str()<<endl;
  }
  outfile.close();
  infile.close();
}

#ifdef CHECK
void check_all() {
  xint how_max=0;
  xint what_max=0;
  for (xint i=1; i<=1000000; i++) {
    xint ret=one_sheep_go(i);
    xint how=ret/i;
    if (how>how_max) {
      how_max=how;
      what_max=i;
    }
    if (0==ret) {
      cout<<"INSOMNIA="<<i<<endl;
    }
    if (0==(i%1000000)) {
      cout<<i<<endl;
    }
  }
  cout<<"ready how_max="<<how_max<<" for "<<what_max<<endl;
  // 72 times for 125
}
#endif

int my_main(int ac, char *av[]) {
  ccharp current_path=(1<ac) ? av[1] : "";
  one_sheep(current_path, "infile.txt", "outfile.txt");
  return 0;
}

