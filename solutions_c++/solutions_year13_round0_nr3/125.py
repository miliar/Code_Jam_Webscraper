fair = []
File.open('/home/prakash/gcj13/qual/c/all_fair').each do |line|
  fair << line.chomp.to_i
end

tc = STDIN.readline.chomp.to_i

tc.times do |t|
  line = STDIN.readline
  a,b = (line.chomp.split).map(&:to_i)

  c=0
  fair.each do |x|
    c+=1 if x>=a && x<=b
  end
  puts "Case ##{t+1}: #{c}"
end
