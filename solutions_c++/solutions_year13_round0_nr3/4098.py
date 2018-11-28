def is_poly(s):
   if s == '': return True
   if s[0] != s[-1]: return False
   return is_poly(s[1:-1])

print [(i * i) for i in xrange(10**7 + 100) if is_poly(str(i)) and is_poly(str(i * i))]
